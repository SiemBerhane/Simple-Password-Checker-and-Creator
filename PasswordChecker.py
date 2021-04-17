import random

def MainMenu():
    # Making sure the user enters a valid value
    try:
        userInput = int(input("Press 1 to check your password\nPress 2 to generate a new password\n>>> "))
    except ValueError:
        print("Please enter a valid character")
        MainMenu()

    if userInput == 1:
        CheckPassword()
    elif userInput == 2:
        CreatePassword()
    else:
        print("Please enter a valid number")
        MainMenu()


def CheckPassword():    
    numOfNumbers = 0
    numOfUpper = 0
    numOfLower = 0

    userPassword = input("Please enter your password\n>>> ")    

    # Error handling
    while len(userPassword) < 6:
        userPassword = input("The password you entered is too short, please try again\n>>> ")

    # Loops through the user's password and checks if it passess all the criteria
    for i in range (len(userPassword)):
        # Converts the character in to ASCII        
        asciiLetter = ord(userPassword[i]) 

        # Checks to see if the ASCII matches with the corresponging numbers
        if asciiLetter > 64 and asciiLetter < 91:
            numOfUpper += 1
        
        elif asciiLetter > 96 and asciiLetter < 123:
            numOfLower += 1

        elif asciiLetter > 47 and asciiLetter < 58:
            numOfNumbers += 1
        
    if numOfNumbers == 0 or numOfUpper == 0 or numOfLower == 0:
        print ("You must include a number and a lower and upper case letter in your password")
        CheckPassword()
    else:
        print ("Your password is nice and strong")

    MainMenu()

def CreatePassword():
    password = ""        

    # Loops through the legnth of the password  
    for typeOfCharacter in range(20):
        typeOfCharacter = random.randint(1, 4)
        
        if typeOfCharacter == 1:  # Number
            randomAsciiNum = random.randint(48, 57)
            password += ConvertAsciiToString(randomAsciiNum)
        
        elif typeOfCharacter == 2:  # Uppercase
            randomAsciiNum = random.randint(65, 90)
            password += ConvertAsciiToString(randomAsciiNum)

        elif typeOfCharacter == 3:  # Lowercase
            randomAsciiNum = random.randint(97, 122)
            password += ConvertAsciiToString(randomAsciiNum)

        elif typeOfCharacter == 4:  # Special
            randomAsciiNum = random.randint(33, 47)
            password += ConvertAsciiToString(randomAsciiNum)

    print("Your password is", password)

    MainMenu()


def ConvertAsciiToString(asciiNum):
    return chr(asciiNum)



MainMenu()
