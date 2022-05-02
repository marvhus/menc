# ASCII table
alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# decrypt the encrypted text
def mdenc(_encrypedText, _key):
    # Calculate the indexes of the characters in the encrypted text, based of the alphabet variable
    encryptedTextCharIndex = []
    for char in _encrypedText:
        index = alphabet.index(char)
        if index == -1:
            print(f"error, illegal character: \"{char}\"")
            return
        encryptedTextCharIndex.append(index)

    # Decrypt the text
    decrypted = ""
    for i in range(len(_key)):
        charIndex = (encryptedTextCharIndex[i % len(encryptedTextCharIndex)] - _key[i]) % len(alphabet)
        char = alphabet[charIndex]
        decrypted += char

    # Print out the decrypted text
    print(f"\nThe decrypted string:\n-\t{decrypted}\n")

# Main function
def main(_encryptedText, _encryptionKey):
    n = 2
    key = [_encryptionKey[i:i+n] for i in range(0, len(_encryptionKey), n)]
    for i in range(len(key)):
        key[i] = int(key[i], 16)

    mdenc(_encryptedText, key)

# Startup
if __name__ == '__main__':
    import argparse as ap

    parser = ap.ArgumentParser()

    # -eT "World" -eK "[15, 10, 6, 0, -11]"
    parser.add_argument('-eT', '--encryptedText', dest = 'encryptedText', help = 'the encrypted text', type = str)
    parser.add_argument('-eK', '--encryptionKey', dest = 'encryptionKey', help = 'the encryption key', type = str)

    args = parser.parse_args()

    import sys
    if args.encryptedText is None:
        print("Error, expected flag \"-eT\"")
        sys.exit(1)
    elif args.encryptionKey is None:
        print("Error, expected flag \"-eK\"")
        sys.exit(1)
    else:
        main(args.encryptedText, args.encryptionKey)


