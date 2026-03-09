import base64

def rot13(message):
    decoded_message = ''
    for char in message:
        if char.isalpha():
            shift = 13
            if char.islower():
                decoded_message += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decoded_message += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decoded_message += char
    return decoded_message

def unhex(hex_string):
    a=["".join(hex_string[i:i+2]) for i in range(0,len(hex_string),2)]
    a=[i for i in a if i != "0x"]
    return "".join([chr(int(i,16)) for i in a])

def base64d(encoded_string):
    return base64.b64decode(encoded_string).decode('utf-8')

def big_int(hex_string):
    a=["".join(hex_string[i:i+2]) for i in range(0,len(hex_string),2)]
    a=[i for i in a if i != "0x"]
    return "".join([chr(int(i), 16) for i in a])

def utf(encoded_data):
    if isinstance(encoded_data, list):
        encoded_data = ''.join(chr(byte) for byte in encoded_data)
        return encoded_data.encode('latin1').decode('utf-8')
    elif isinstance(encoded_data, str):
        return encoded_data.encode('latin1').decode('utf-8')
    else:
        raise ValueError("Format de données non supporté pour le décodage UTF-8")
