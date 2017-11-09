import random
from Crypto.Util import number

def readFile(funName, fileName):
    try:
        with open(fileName, 'r') as f:
            return f.read()
            
    except FileNotFoundError:
        print("{0}: key file: {1} not found".format(funName, fileName))
        exit()
    
def enc(keyFile, inputFile, outputFile):
    
    key = readFile('rsa-enc', keyFile).split('\n')
    if len(key) != 3:
        print("rsa-enc: invalide key file")
        exit()
    
    else: # Pull info from public key
        nBits = int(key[0])
        n = int(key[1])
        e = int(key[2])
    
    plainText = readFile('rsa-enc', inputFile)
    
    print(plainText)
    # print(bin(int(plainText)))
    
    # Add the padding to the plain text
    r = random.getrandbits(nBits // 2)
    r = r << (nBits - (nBits // 2) - 2)
    m = r + int(plainText)
    
    # print(m)
    # print(bin(m))
    
    # Calculate the cypher text
    cipherText = pow(m, e, n)
    
    print(cipherText)
    # print(bin(cipherText))
    
    with open(outputFile, 'w+') as o:
        o.write(str(cipherText))

def dec(keyFile, inputFile, outputFile):
    
    key = readFile('rsa-dec', keyFile).split('\n')
    if len(key) != 3:
        print("rsa-dec: invalide key file")
        exit()
    
    else: # Pull the info from the private key
        nBits = int(key[0])
        n = int(key[1])
        d = int(key[2])
    
    cipherText = readFile('rsa-dec', inputFile)
    
    print(cipherText)
    # print(bin(int(cipherText)))
    
    # Calculate the plain text with the padding
    m = pow(int(cipherText), d, n)
    # print(m)
    # print(bin(m))
    # Pull off the padding
    plainText = m & ((1 << nBits - (nBits // 2) - 2) - 1)
    
    print(plainText)
    # print(bin(int(plainText)))
    
    with open(outputFile, 'w+') as o:
        o.write(str(plainText))
    
def isPrime(n):
    if n < 2:
        return False
        
    d = n - 1
    t = 0
    while d % 2 == 0:
        d = d // 2 #Apparently the // operator explicitly does integer division. Cool.
        t += 1
        
    for k in range(5):
        a = random.randint(2, n - 2)
        v = pow(a, d, n)
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                    
                else:
                    i += 1
                    v = pow(v, 2) % n
                    
    return True
    
def getRandPrime(n):
    prime = 1
    while not isPrime(prime):
        random.randint(2, n)
        
    return prime
    
def isCoprime(x, y):
    for z in range(2, min(x, y) + 1):
        if (x % z) == (y % z) == 0:
            return False
            
    return True
    
def getCoprime(order):
    for e in range(3, order):
        if isCoprime(e, order):
            return e
        
    print("didn't find coprime with {0}".format(order))
    exit()

def keygen(pubKeyFile, privKeyFile, numBits):
    
    p = number.getPrime(int(numBits))
    q = number.getPrime(int(numBits))
    print(p)
    print(q)
    n = p * q
    order = (p - 1) * (q - 1)
    e = getCoprime(order)
    print(n)
    print(order)
    print(e)
    d = 1 / (e % order)
    print(d)
    