from __future__ import print_function, unicode_literals
from os import urandom
import sys
import codecs

#takes byte strings and xor's them
def xorByteString(s1,s2):
    return bytes(s1 ^ s2 for s1, s2 in zip(s1,s2))

def main():
    byteString1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    byteString2 = bytes.fromhex('686974207468652062756c6c277320657965')

    print(xorByteString(byteString1,byteString2).hex())

if __name__ == '__main__':
    main()
