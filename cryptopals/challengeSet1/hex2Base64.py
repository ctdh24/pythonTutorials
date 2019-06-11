import sys
import base64



def hexStr2Base64(hexstring):
    decodedHexString = bytes.fromhex(hexstring)
    decodedBase64 = base64.b64encode(decodedHexString)
    return decodedBase64.decode()

def main():
    var = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print ("Challenge - Convert hex to base64")
    print(hexStr2Base64(var))

if __name__ == '__main__':
    main()
