import utils

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

mostFrequentLetters = {"english": ["e","n","i","r","s","a","t","d","h","u","l",
                                   "g","o","c","m","b","f","w","k","z","p","v",
                                   "j","y"],
                       "croatian":["a","i","o","e","n","s","r","j","t","u","d",
                                   "k","v","l","m","p","c","z","g","b","h","f"]}

mostFrequentBigrams = {"english":["th","he","an","in","er","re","on","es","ti","at"],
                       "croatian":["je","na","ra","st","an","ni","ko","os","ti","ij","n"]}

def cipherIndex(cipherKey, currentIndex):
    return divmod(cipherKey + currentIndex, len(alphabet))[1]

def singleKeyCaesarAlphabet(cipherKey):
    # Prints Caesar alphabet with shift of value cipherKey
    cipherAlphabet = {}
    for i in range(26):
        currentLetter = alphabet[i]
        cipherLetter = alphabet[cipherIndex(cipherKey, i)]
        cipherAlphabet[currentLetter] = cipherLetter
    return cipherAlphabet

def printFrequency(text, content, shouldPrint="false"):
    if shouldPrint:
        print(text, content)
    return

def letterFrequency(cipher, shouldPrint="false"):
    # (string) -> dict
    # For a given string, returns a dictionary with keys being alphabet letters, 
    # and values their frequency in a given string, sorted by frequency
    frequency = {}
    for letter in alphabet:
        frequency[letter] = cipher.count(letter)
    letterFrequencies = utils.sortFrequency(frequency)
    printFrequency("Letter frequencies: ", letterFrequencies, shouldPrint)
    return letterFrequencies

def bigramFrequency(cipher, shouldPrint="false"):
    # (string) -> dict
    # For a given string, returns a dictionary with keys being bigrams that appear in string, 
    # and values their frequency in a given string, sorted by frequency
    frequency = {}
    for i in range(len(cipher)-1):
        currentBigram = str(cipher[i] + cipher[i+1])
        frequency[currentBigram] = cipher.count(currentBigram)
    bigramFrequencies = utils.sortFrequency(frequency)
    printFrequency("Bigram frequencies: ", bigramFrequencies, shouldPrint)
    return bigramFrequencies

def singleKeyCaesar(text, shift=3, flag="encode"):
    # Encode or decode (flag) text with Ceasar cipher with single shift
    cipher = ""
    cipherAlphabet = singleKeyCaesarAlphabet(shift) if (flag == "encode") else singleKeyCaesarAlphabet(-shift)
    for letter in text:
        if (letter != " "):
            cipher += cipherAlphabet[letter]
    return cipher

def calculateShift(first, second):
    firstIndex = alphabet.index(first)
    secondIndex = alphabet.index(second)
    return firstIndex - secondIndex

def guessSingleKeyCaesar(cipher, language="english"):
    # Encoding cipher in a given language
    frequentLettersInLanguage = mostFrequentLetters[language]
    frequentLettersInCipher = letterFrequency(cipher)
    pivotLetter = frequentLettersInCipher[0][0]
    
    guessed = "no"
    currentIndex = 0
    while (currentIndex < 21):
        # Try matching the most frequent letter in cipher with
        # the most frequent letter in a given language
        # If user inputs no, continue the process by moving onto the next letter
        currentPivot = pivotLetter
        currentGuess = frequentLettersInLanguage[currentIndex]
        currentShift = calculateShift(currentPivot, currentGuess)
        text = singleKeyCaesar(cipher, currentShift, "decode")
        print(text)
        guessed = input("Was this correct? (yes / no): ")
        if (guessed == "yes"):
            break
        currentIndex += 1
    return text

def replaceLetters(letterList, cipher):
    # needs to skip already checked letters
    for key, value in letterList:
        cipher = cipher.replace(key, value)
    return cipher
