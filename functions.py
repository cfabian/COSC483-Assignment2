from multiprocessing import Process
import operator
import os
from Crypto.Cipher import AES
import sys
from multiprocessing import Process,Manager, Pool
import multiprocessing as mp
import binascii

blocksize = 128
keysize = 256





def padding(raw):

    lraw = len(raw[-1])*8
    modraw = lraw % blocksize
    remainder = blocksize - modraw
    # print("modraw:",modraw)
    if modraw == 0:
        remainder = 128
        paddingstr = (int(remainder/8)).to_bytes(int(remainder/8),byteorder="big",signed=False)* int(remainder/8)
        # print("Padding str",paddingstr)
        # raw.append(bytes("\0", encoding='utf-8') * int(((remainder)/(len(bytes("\0", encoding='utf-8')) * 8))))
        raw.append(paddingstr)
    else:
        # paddingstr = bytes(str(remainder),encoding='utf-8') * int(((remainder)/(len(bytes(str(remainder), encoding='utf-8')) * 8)))
        paddingstr = (int(remainder / 8)).to_bytes(1, byteorder="big", signed=False) * int(remainder/8)
        # print(paddingstr)
        # print("Padding str", int(remainder / 8))
        raw[-1] = raw[-1] + paddingstr

    return raw


def remove_padding(raw):
    #needs some love
    i = int.from_bytes(raw[-1][-1:],byteorder="big",signed=False)
    raw[-1] = raw[-1][:16 - i]
    return raw


def XOR(a, b):# https://stackoverflow.com/questions/29408173/byte-operations-xor-in-python
    return bytes(map(operator.xor, a, b))


# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n): # https://chrisalbon.com/python/break_list_into_chunks_of_e
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]


def IV_Gen():
    return os.urandom(int(blocksize/8))

