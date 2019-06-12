import base64

def singleCipherXOR(inputBytes, cipher):
    outputBytes = b''
    for byte in inputBytes:
        outputBytes += bytes([byte ^ cipher])
    return outputBytes

def englishScoring(inputBytes):
    letterFrequencies = {
        'a': .08167,
        'b': .01492,
        'c': .02782,
        'd': .04253,
        'e': .12702,
        'f': .02228,
        'g': .02015,
        'h': .06094,
        'i': .06094,
        'j': .00153,
        'k': .00772,
        'l': .04025,
        'm': .02406,
        'n': .06749,
        'o': .07507,
        'p': .01929,
        'q': .00095,
        'r': .05987,
        's': .06327,
        't': .09056,
        'u': .02758,
        'v': .00978,
        'w': .02360,
        'x': .00150,
        'y': .01974,
        'z': .00074,
        ' ': .13000
    }
    return sum([letterFrequencies.get(chr(byte),0) for byte in inputBytes.lower()])

def main():
    string2Decode = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    cipherText = bytes.fromhex(string2Decode)
    messagesArr = []
    for key_cipher in range(256):
        message = singleCipherXOR(cipherText,key_cipher)
        score = englishScoring(message)
        data = {'message': message, 'score': score, 'key': key_cipher}
        messagesArr.append(data)
    best_score = sorted(messagesArr, key=lambda x: x['score'], reverse=True)[0]
    for item in best_score:
        print("{}: {}".format(item.title(), str(best_score[item])))

if __name__ == '__main__':
    main()
