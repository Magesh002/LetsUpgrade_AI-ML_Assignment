s = input("Enter the input string: ")


def removeSpecialCharsWithLowerCase(inputString):
    return ''.join(string for string in inputString if string.isalnum()).lower()


print("The result for the given input string is:", removeSpecialCharsWithLowerCase(inputString=s))