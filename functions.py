
def readFile(funName, fileName):
    try:
        with open(fileName, 'r') as f:
            return f.read()
            
    except FileNotFoundError:
        print("{0}: key file: {1} not found".format(funName, fileName))
        exit()

def enc(keyFile, inputFile, outputFile):
    
    key = readFile('rsa-enc', keyFile).split('\n')
    nBits = int(key[0])
    n = int(key[1])
    e = int(key[2])
    
    plainText = readFile('rsa-enc', inputFile)
    
    print(plainText)
    
    cipherText = pow(int(plainText), e) % n
    
    print(cipherText)
    
    with open(outputFile, 'w+') as o:
        o.write(str(cipherText))

def dec(keyFile, inputFile, outputFile):
    
    key = readFile('rsa-dec', keyFile).split('\n')
    nBits = int(key[0])
    n = int(key[1])
    d = int(key[2])
    
    cipherText = readFile('rsa-dec', inputFile)
    
    print(cipherText)
    
    plainText = pow(int(cipherText), d) % n
    
    print(plainText)

def keygen(pubKeyFile, privKeyFile, numBits):
    
    print(pubKeyFile)
    print(privKeyFile)
    print(numBits)
    