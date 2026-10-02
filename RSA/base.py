import random

def extGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extGCD(b, a % b) 
    x = y1 
    y = x1 - (a//b)*y1
    return g, x, y

def invMod(a, m):
    g, x, _ = extGCD(a, m)
    if g != 1:
        raise ValueError(f'invMod: gcd is not 1, therefore a modular inverse does not exist!')
    return x % m

def powMod(a, e, m):
    res = 1
    a = a % m
    while e > 0:
        if e & 1:
            res = (res * a) % m
        a = (a * a) % m
        e = e >> 1
    return res

def millerTest(n, d):
    a = random.randint(2, n-2)
    x = powMod(a, d, n)
    if x == 1 or x == n-1:
        return True
    while d != n-1:
        x = (x*x) % n    # faster than powMod for this specific case
        d *= 2
        if x == 1:
            return False
        elif x == n - 1:
            return True
    return False

def primeCheck(n, effVal):
    i = 0
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if (n & 1) == 0:
        return False
    d = n-1
    while (d & 1) == 0:
        d //= 2
    while i < effVal:
        x = millerTest(n, d)
        if x == False:
            return False
        i += 1
    return True

def primeGen():
    while True:
        bits = ['1']
        for i in range(22):
            bits.append(str(random.randint(0, 1)))
        bits.append('1')
        num = int(''.join(bits), 2)
        if primeCheck(num, 20) == True:
            return num

p = primeGen()
q = primeGen()
print(f'p = {p}')
print(f'q = {q}')
n = p * q
phi = (p-1) * (q-1)

e = 65537

g, _, _ = extGCD(e, phi)
if g != 1:
    g, _, _ = extGCD(e, phi)

d = invMod(e, phi)

#public key = (n, e)
#private key = (n, d)

#this is just to illustrate with a random plaintext
m = random.randint(0, 1230)
c = powMod(m, e, n)
print(f'{m} -> {c}', end = '')
m1 = powMod(c, d, n)
print(f' -> {m1}')