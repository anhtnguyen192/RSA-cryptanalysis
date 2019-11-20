import textmalnipulation
import encrypt
import cryptanalysis

def readFileText():
    f = open("plaintext.txt","r")
    contents = f.read()
    return contents

def readFileKey():
    f = open("publickey.txt","r")
    contents = f.read()
    return contents

def readFileCipher():
    f = open("ciphertext.txt","r")
    contents = f.read()
    return contents

def strListToIntList(sl):
    cC = []
    for i in range(0, len(sl) - 1): 
        cC.append(int(sl[i]))
    return cC

plainText = readFileText()
key = readFileKey().split(" ")
cipherText = readFileCipher().split(" ")

encrypt.encryption(int(key[0]), textmalnipulation.hashing(plainText), int(key[1]))
cryptanalysis.decryption(int(key[0]), strListToIntList(cipherText), int(key[1]))
