def removeSpaces(text):
    return text.replace(" ","")

def removeNumbers(text):
    return ''.join(i for i in text if not i.isdigit())

def cleanInput(text):
    # Removes whitespaces from text and returns lowercase text
    return removeSpaces(removeNumbers(text)).lower()

def sorting(dictionary):
    # Sorting dictionary by values
    return sorted(dictionary.items(), key = lambda x: x[1], reverse = True)

def removeZeroes(dictionary):
    # Removes items that have value 0 from given dictionary
     return {x:y for x,y in dictionary.items() if y!=0}

def sortFrequency(dictionary):
    return sorting(removeZeroes(dictionary))
