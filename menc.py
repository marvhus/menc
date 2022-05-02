# ASCII table
alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# Encrypt the text
def menc(_Input, _Output):
    # Calculate the indexes of the characters in the input based of the alphabet variable
    inputArr = []
    for char in _Input:
        index = alphabet.index(char)
        if index == -1:
            print(f"Error: illegal character: '{char}'")
            return
        inputArr.append(index)

    # Calculate the indexes of the character in the output based of the alphabet variable
    outputArr = []
    for char in _Output:
        index = alphabet.index(char)
        if index == -1:
            print(f"Error: illegal character: '{char}'")
            return
        outputArr.append(index)

    # Calculate the encryption/decryption key
    key = ""
    for i in range(len(inputArr)):
        inputCharIndex = inputArr[i]
        outputCharIndex = outputArr[i % len(outputArr)]

        difference = None
        if inputCharIndex == outputCharIndex:
            difference = 0
        elif inputCharIndex < outputCharIndex:
            difference = outputCharIndex - inputCharIndex
        elif inputCharIndex > outputCharIndex:
            difference = len(alphabet) - (inputCharIndex - outputCharIndex)
        else:
            print("This shouldn't happen")
            return

        # Check if the difference is correct
        if outputCharIndex == (inputCharIndex + difference) % len(alphabet):
            hexValue = "%0.2X" % difference
            key += hexValue
        else:
            print("error, could not find the charIndex difference")

    # Tell the user what the encryped text is, and the key to encrypt/decrypt it
    print(f"\nthe generated key:\n-\t\"{key}\"\n\nthe encrypted string:\n-\t\"{_Output}\"")

    # Testing if it decrypt corectly
    decrypted = ""
    n = 2
    keyList = [key[i:i+n] for i in range(0, len(key), n)]
    for i in range(len(keyList)):
        value = int(keyList[i], 16)
        charIndex = (outputArr[i % len(outputArr)] - value) % len(alphabet)
        char = alphabet[charIndex]
        decrypted += char

    # print out the decrypted result from the encrypted text, to test if it works
    print(f"\nthe decrypted text:\n-\t\"{decrypted}\"\n")

# main function
def main(_input, _output):
    if len(_output) < len(_input):
        print("\nIt is recomended to have a output text at least as long as the input text\n")

    menc(_input, _output)

# startup
if __name__ == '__main__':
    import argparse as ap

    parser = ap.ArgumentParser()

    # -iT "Hello, World!" -oT "Wazzzzzzzzzup"
    parser.add_argument('-iT', '--inputText',  dest = 'inputText',  help = 'the text to be encrypted', type = str)
    parser.add_argument('-oT', '--outputText', dest = 'outputText', help = 'the encryped output text', type = str)

    args = parser.parse_args()

    import sys
    if args.inputText is None:
        print("Error, expected flag \"-iT\"")
        sys.exit(1)
    elif args.outputText is None:
        print("Error, expected flag \"-oT\"")
        sys.exit(1)
    else:
        main(args.inputText, args.outputText)



