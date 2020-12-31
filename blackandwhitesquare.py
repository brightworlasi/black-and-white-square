def main():
    counter = 1
    while counter != 0:
        valuePair = input("Enter the two values, Example 'a1' or 'A1': ")
        splitValueForCharacter = valuePair[0]
        splitValueForNumber = int(valuePair[1])
        returnedValue = numberASCIICode(splitValueForCharacter)
        if (returnedValue == 97) and (splitValueForNumber == 1):
            print("The square is Black")
        elif (returnedValue % 2) == 0 and (splitValueForNumber % 2 == 0):
            print("The square is Black")
        elif (returnedValue % 2) == 1 and (splitValueForNumber % 2 == 1):
            print("The square is Black")
        else :
            print("The square is white")
        counter = int(input("Check another number? Press 1 for YES and 0 for NO: "))
def numberASCIICode(a):
    letter = a.lower()
    asciiValue = ord(letter)
    return asciiValue
main()


