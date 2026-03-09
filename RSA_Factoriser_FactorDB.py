from Crypto.Util.number import long_to_bytes
from factordb.factordb import FactorDB
n = N
p = 0
q = 0
f = FactorDB(n);f.connect()
r = f.get_factor_list()
p = int(r[0]); q = int(r[1])
d = inverse(e, (p-1)*(q-1))
flag = long_to_bytes(pow(c, d, n))
print("P: ",p,"\n","Q: ",q,"\n","FLAG: ",flag)