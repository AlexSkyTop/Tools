file = open("whitepages.txt","r", encoding="utf-8").read()
data1 = ["1" if i==" " else "0" for i in file]; 
data1 = [i for i in data1 if i != " "]
data2 = ["0" if i==" " else "1" for i in file]; 
data2 = [i for i in data2 if i != " "]
flag1 = [chr(int("".join(data1[i:i+8]), 2)) for i in range(0, len(data1), 8)]
flag2 = [chr(int("".join(data2[i:i+8]), 2)) for i in range(0, len(data2), 8)]
print("".join(flag1))
print("\n\n", "".join(flag2))