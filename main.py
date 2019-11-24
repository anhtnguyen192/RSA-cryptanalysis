import textmal
import encrypt
import cryptanalysis

def read_file_text():
    f = open("plaintext.txt","r")
    contents = f.read()
    return contents

def read_file_key():
    f = open("publickey.txt","r")
    contents = f.read()
    return contents

def read_file_cipher():
    f = open("ciphertext.txt","r")
    contents = f.read()
    return contents

def strlist_to_intList(sl):
    cC = []
    for i in range(0, len(sl) - 1): 
        cC.append(int(sl[i]))
    return cC

def menu():
    print("\n1. Encrypt\n2. Cryptanalysis\n3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        plainText = read_file_text()
        encrypt.encryption(int(key[0]), textmal.hashing(plainText), int(key[1]))
        menu()
    elif choice == '2':
        cipherText = read_file_cipher().split(" ")
        cryptanalysis.decryption(int(key[0]), strlist_to_intList(cipherText), int(key[1]))
        menu()
    elif choice == '3':
        exit
    else:
        menu()


key = read_file_key().split(" ")
menu()
