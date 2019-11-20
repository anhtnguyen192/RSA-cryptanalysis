def squareAndMultiply(e,hC,n):
    biOfE = bin(e) 
    z = 1
    for i in range(0,len(biOfE) ):
        z = (z * z) 
        if biOfE[i] == '1':
            z = (z * hC) 
        z = z % n
    return z

def encryption(keyE, hC, keyN):
    f = open("ciphertext.txt","w")
    for x in hC:
        s = squareAndMultiply(keyE, x, keyN)
        f.write(str(s))
        f.write(' ')

