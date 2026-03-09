
# cet outil permet de créer des pattern lorsque gdb ou d'autre outil ne sont pa disponoble
def make(n):
    alpha_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_min = alpha_maj.lower()
    alpha_num = "0123456789"
    pattern = ""
    for i in alpha_maj:
        for j in alpha_min:
            for k in alpha_num:
                pattern += i+j+k 
                if len(pattern) >= n:break 
    while len(pattern) != n:pattern = pattern[:-1]
    return pattern

size = input("Enter size : ")
if size :
    rep = make(int(size))
    print("Pattenr : ", rep)
    print("Size : ", len(rep))