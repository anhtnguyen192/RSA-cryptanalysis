import math
import encrypt
import textmalnipulation
import random

'''
def isPerfectSquare(x): 
    sr = math.sqrt(x) 
    return ((sr - math.floor(sr)) == 0) 

def fermatFactoring(n):
    s = int (math.sqrt(n)) + 1 
    while isPerfectSquare(s * s - n) == False:
        s += 1
    return s - math.sqrt(s*s - n), s + math.sqrt(s*s - n)
'''

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b


def brent(N):
    if N % 2 == 0:
        return 2, N // 2
    y, c, m = random.randint(1, N - 1), random.randint(1, N - 1), random.randint(1, N - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % N + c) % N
        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            k = k + m
        r *= 2
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            if g > 1:
                break

    return g, N // g

def egcd(a, b):
    mod = b
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    if x < 0:
        x += mod
    return gcd, x, y

def decryptEachWord(e,x,n):
    f = brent(n)
    #print(f[0], f[1])
    phi = (f[0] - 1) * (f[1] - 1)
    d = egcd(e, phi)[1]
    return encrypt.squareAndMultiply(int(d),x,n)
    
def decryption(keyE, cT, keyN):
    f = open("decryptedtext.txt","w")
    hC = []
    for x in cT:
        t = decryptEachWord(keyE, x, keyN)
        hC.append(t)
        f.write(str(textmalnipulation.unhashing(t)))
        f.write(' ')
    


