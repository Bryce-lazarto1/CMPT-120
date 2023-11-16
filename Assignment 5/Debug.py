def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("Enter an int: ")
    if intInput.isdigit():
        print("Int!")
    else:
        print("Not int :(")

    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers: ")

    if any(char.isalpha() for char in alphIntInput) and any(char.isdigit() for char in alphIntInput):
        print("Letters and numbers!")
    else:
        print("Weird characters :(")
       
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")
        
    #now write code to check if the input was either an asterisk OR an ampersand (&)
    symbolInput = input("Enter a symbol (* or &): ")
    if symbolInput == '*' or symbolInput == '&':
        print("correct symbol!")
    else:
        print("incorrect symbol :(")
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    userInput = input("Enter an integer: ")

    if userInput.isdigit():
        integerInput = int(userInput)
        print("that is a integer:", integerInput)
    else:
        print("wrong input enter correct integer.")

    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
    userInput = input("Enter a string: ")

    if "marist" in userInput:
        print("The substring 'marist' is there")
    else:
        print("The substring 'marist' is not there.")
main()
