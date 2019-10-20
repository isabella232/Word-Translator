def createAlphabet(charEncoding):
    ''' Turns a 26 character string called charEncoding into a dictionary,
        pairing each English letter to each character

        Input: "abcdefghijklmnopqrstuvwxyz"
        Output: {0: 'a', 1: 'b', 2: 'c', ... , 24: 'y', 25: 'z'}
    '''

    # obtain user input
    while (True):
        print("Please enter 26 characters for your new alphabet")
        print("The first character replaces 'a', and the last character replaces 'z'")
        encoding = input()

        if (len(encoding) == 26):
            break
        print("Not 26 characters")

    # declare necessary variables
    newAlphabet = {}
    engAlphabet = "abcdefghijklmnopqrstuvwxyz"

    # create the new alphabet
    i = 0
    for newChar in charEncoding:
        engChar = engAlphabet[i]
        newAlphabet[engChar] = newChar
        i += 1

    return newAlphabet

def translate(alphabet, word):
    ''' Uses a dictionary called alphabet to translate word
        Does not modify original word

        alphabet has elements (englishChar : translatedChar)
        word is a string
        
        Inputs: Dictionary, string
        Output: string
    '''

    newWord = ""
    for char in word:
        newWord += alphabet[char]

    return newWord

def main():
    ''' Translates a single word into another word using a new alphabet
        First, creates dictionary of new alphabet, then continuously asks
        user for words to translate and prints out the translation until they
        type Enter
    '''

    # generate pseudo-alphabet and store into dictionary
    newAlphabet = createAlphabet(encoding)
    
    # translate words until user ends program
    while (True):
        print("Enter a word to translate using the new encoding (Enter to exit)")

        engWord = input("Old Word: ")

        if (engWord == ""):
            break
        
        # generate word using newly defined alphabet
        word = translate(newAlphabet, engWord)

        print("New Word: " + word + "\n")
