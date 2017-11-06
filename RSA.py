import functions
import sys

if __name__ == "__main__":# Need some shit about the special way we are going to have him run our code
    # mode = ''
    # raw = bytes('', encoding='utf-8')
    # key = bytes('', encoding='utf-8')
    # iv = None
    # keyFile = None
    # inputFile = None
    # outputFile = None
    # ivFile = None
    
    if not (len(sys.argv) == 8):
        print(len(sys.argv))
        print("Usage: ./[rsa-enc/rsa-dec/rsa-keygen]")
        print("          -k <key file> : required, specifies a file storing a valid RSA key in the example format")
        print("          -i <input file> : required, specifies the path of the file containing an integer in Z∗n in String form (base 10) that is being operated on")
        print("          -o <output file> : required, specifies the path of the file where the resulting output is stored in String form (base 10)")
        exit()
        
    elif sys.argv[1] == 'rsa-enc':
        print("Do RSA Encryption")
        
    elif sys.argv[1] == 'rsa-dec':
        print("Do RSA Decryption")
        
    elif sys.argv[1] == 'rsa-keygen':
        print("Do RSA Key Generation")
        
        
    
    # if len(sys.argv) <= 6:
    #     print("Usage: ./[cbc-enc/cbc-dec/ctr-enc/ctr-dec] -k keyFile -i inputFile -o outputFile (-v ivFile)")
    #     exit()
    # else:
    #     mode = sys.argv[1]
    #     print(mode)
    #     for i in range(2, len(sys.argv)):
    #         if sys.argv[i] == '-k':
    #             keyFile = sys.argv[i+1]
    #             file = open(keyFile, 'rb')
    #             for line in file:
    #               key += line
    #             key = binascii.unhexlify(key)
    #         elif sys.argv[i] == '-i':
    #             inputFile = sys.argv[i+1]
    #         elif sys.argv[i] == '-o':
    #             outputFile = sys.argv[i+1]
    #         elif sys.argv[i] == '-v':
    #             ivFile = sys.argv[i+1]
    #             file = open(ivFile, 'rb')
    #             iv = bytes('', encoding='utf-8')
    #             for line in file:
    #                 iv += line
    # if keyFile == None or inputFile == None or outputFile == None:
    #     print(sys.argv)
    #     print("Usage: ./[cbc-enc/cbc-dec/ctr-enc/ctr-dec] -k keyFile -i inputFile -o outputFile (-v ivFile)")
    #     exit()
    # if iv == None:
    #     iv = IV_Gen()
    # #TODO: get key and raw from files, the files are hex encoded
    # #key = bytes("1234567890abcdef1234567890abcdef", encoding='utf-8')
    # #raw = bytes("1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdefads", encoding='utf-8')
    # output = open(outputFile, 'wb')
    # input = open(inputFile, 'rb')

    # for line in input:
    #     raw += line
    # if mode == 'cbc-enc':
    #     ct = cbc_enc(key,raw,iv)
    #     print('CipherText (CBC): ', ct)
    #     output.write(ct)
    # elif mode == 'cbc-dec':
    #     dt = cbc_dec(key, raw)
    #     print('PlainText (CBC): ', dt)
    #     output.write(dt)
    # elif mode == 'ctr-enc':
    #     ct = ctr_enc(key, raw, iv)
    #     print('CipherText (CTR): ', ct)
    #     output.write(ct)
    # elif mode == 'ctr-dec':
    #     dt = ctr_dec(key, raw)
    #     print('PlainText (CTR): ', dt)
    #     output.write(dt)
    # else:
    #     print("Invalid Mode")
    #     exit()

    # output.close()
    # input.close()