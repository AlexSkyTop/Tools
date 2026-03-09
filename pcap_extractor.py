from scapy.all import rdpcap

file_name = input("file name : ")
p = rdpcap(file_name)

result = []

for packet in p :
    if packet.haslayer("Raw") :
        d = packet["Raw"].load
        result.append(d)
r = b"\n#########\n".join(result)

open("result","wb").write(r)
print("end")
