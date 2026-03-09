# x=2%5
# x=3%11
# x=5%17

l5 = [] ; l11=[] ; l17=[]

n=2
c = 0
while True:
    n += 5
    if n%5==2:
       l5.append(n);c += 1
    if c==1000:break

n=3
c = 0
while True:
    n += 11
    if n%11==3:
       l11.append(n);c += 1
    if c==1000:break


n=5
c = 0
while True:
    n += 17
    if n%17==5:
       l17.append(n);c += 1
    if c==1000:break

for i in range(10000):
	if i in l5 and i in l11 and i in l17:
		print(i, i%935)