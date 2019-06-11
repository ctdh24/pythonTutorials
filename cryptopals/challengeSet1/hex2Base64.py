import sys
import codecs

var = sys.argv[1]
print "Challenge - Convert hex to base64"

encoded64P2 = var.decode("hex").encode("base64")
print "Python 2 encoding: " + encoded64P2

encoded64P3 = codecs.encode(codecs.decode(var, 'hex'), 'base64').decode()
print "Python 3 encoding: " + encoded64P3
