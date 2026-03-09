import wave
import struct

def extract_lsb_data(wav_filename, num_lsb=1):
    with wave.open(wav_filename, 'rb') as wav_file:
        n_channels = wav_file.getnchannels()
        samp_width = wav_file.getsampwidth()
        n_frames = wav_file.getnframes()
        frames = wav_file.readframes(n_frames)
        if samp_width == 2:
            fmt = '<h'  # 16-bit signed, little-endian
        elif samp_width == 1:
            fmt = '<B'  # 8-bit unsigned
        else:
            fmt = '<i' if samp_width == 4 else None
            if fmt is None:
                raise ValueError(f"Unsupported sample width: {samp_width}")
        sample_count = len(frames) // samp_width
        samples = []
        for i in range(0, len(frames), samp_width):
            sample = struct.unpack(fmt, frames[i:i+samp_width])[0]
            samples.append(sample)
        bits = []
        for sample in samples:
            for bit_index in range(num_lsb):
                bit = (sample >> bit_index) & 1
                bits.append(bit)
        bytes_data = bytearray()
        for i in range(0, len(bits) - 7, 8):
            byte_val = 0
            for j in range(8):
                byte_val |= (bits[i + j] << j)  # LSB first
            bytes_data.append(byte_val)
        return bytes_data

if __name__ == "__main__":
    wav_file = "mission.wav"
    print("Extracting data from LSB...")
    extracted_data = extract_lsb_data(wav_file, num_lsb=1)
    print(f"Extracted {len(extracted_data)} bytes")
    with open("reslt", "wb") as f:f.write(extracted_data)
