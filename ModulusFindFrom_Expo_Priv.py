"""
pour cela, connectez vous instace pour recuperer les parametre, pour le remplcer dans le d et ct.
ensuite lancer l'execution du code. Le code vous donnera un nombre que vosu allez factoriser depuis le site indiquer.
vous devez remplcer les ^ correctement puis le donnez commme entree.
le code prendera ces facteurs et tentra de retrouver le modulos pour decrypter le message et vous l'affichera.
Enfin, vous donnez le message pico qui vous donnera le flag !
BY AlexSky14520 02/03/2025
"""

from Crypto.Util.number import long_to_bytes, bytes_to_long, size, inverse
from math import gcd, prod
import operator
from functools import reduce
import itertools
from factordb.factordb import FactorDB

e = 65537
ct = 65284880035442698529914530132241966457169066139629468638745565587058373837636
d = 67092873846786955427189154346616518100778557489268856145188186732330291449473

kφ = e * d - 1

def parse_pow(x):
    r = x.split('^')
    if len(r) == 1:
        return [int(r[0])]
    else:
        return [int(r[0])] * int(r[1])

print(kφ)
print('insert factors (use https://www.alpertron.com.ar/ECM.HTM) -- make sure to replace powers with "^":')
factors_in = input()

factors = sum([parse_pow(x.strip().replace(' ', '')) for x in factors_in.split('×')], [])
pfac = factors[-1]
qfac = factors[-2]
factors = factors[:-2]
factors.remove(2)
factors.remove(2)

print('computing factors', len(factors))

T127 = 2**127
T129 = 2**129
ITERS = 3 ** len(factors)
steps = 0
pts = set()

for c in itertools.product([0,1,2], repeat=len(factors)):
    steps += 1
    h     =            prod(factors[i] for i, x in enumerate(c) if x == 0)
    psub1 = 2 * pfac * prod(factors[i] for i, x in enumerate(c) if x == 1)
    qsub1 = 2 * qfac * prod(factors[i] for i, x in enumerate(c) if x == 2)
    if h < e and T127 < psub1 < T129 and T127 < qsub1 < T129 and max(psub1+1, qsub1+1) < 2 * min(psub1+1, qsub1+1):
        n = (psub1 + 1) * (qsub1 + 1)
        pt = long_to_bytes(pow(ct, d, n))
        if len(pt) == 16:
            pts.add(pt)
            print("pt : ", pt)
    if steps % 10000 == 0:
        print(steps, '/', ITERS, steps / ITERS)

print(pts)

#picoCTF{7h053_51n5_4r3_n0_m0r3_3858bd66}