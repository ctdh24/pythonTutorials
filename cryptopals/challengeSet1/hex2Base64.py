import sys
import codecs

var = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print ("Challenge - Convert hex to base64")

toBytes = bytes(var)

encoded64P2 = toBytes.decode("hex").encode("base64")
print "Python 2 encoding: " + encoded64P2

encoded64P3 = codecs.encode(codecs.decode(toBytes, 'hex'), 'base64').decode()
print "Python 3 encoding: " + encoded64P3
