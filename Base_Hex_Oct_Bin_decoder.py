def decode_binary(data):
    data = data.replace(" ", "")
    return "".join([chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8)])

def decode_octal(data):
    data = ["0"+i for i in data.split()]
    return "".join([chr(int(i, 8)) for i in data])

def decode_hex(data):
    data = data.replace(" ", "").lower().lstrip('0x')
    return "".join([chr(int(data[i:i+2], 16)) for i in range(0, len(data), 2)])

menu = """
Choisissez le type de codage :
	1 - Binaire
	2 - Octal
	3 - Hexadécimal
"""

while True:
	print(menu)
	choix = input("Votre choix : ")
	data = input("Entrez les nombres : ")
	if choix == "1":print("Résultat :", decode_binary(data))
	elif choix == "2":print("Résultat :", decode_octal(data))
	elif choix == "3":print("Résultat :", decode_hex(data))
	else:print("Choix invalide.")
