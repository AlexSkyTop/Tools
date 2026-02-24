import string

ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")

def unshift(c, k):
    t1 = ALPHABET.index(c)
    t2 = ALPHABET.index(k)
    return ALPHABET[(t1 - t2) % 16]

def b16_decode(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        high = ALPHABET.index(enc[i])
        low  = ALPHABET.index(enc[i+1])
        val = (high << 4) | low
        plain += chr(val)
    return plain

def try_decrypt(cypher, key):
    b16 = ""
    for c in cypher:
        b16 += unshift(c, key)
    decoded = b16_decode(b16)
    return decoded

enc = "fegdeogdgecoeocgcgchcfcffccfca"

for l in ALPHABET:
    decoded = try_decrypt(enc, l)
    print(decoded)