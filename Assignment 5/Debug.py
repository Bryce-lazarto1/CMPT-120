def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
'''isnumeric()'''

    #what about if it's both letters and numbers?
'''isdigit()'''


    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")
        
    #now write code to check if the input was either an asterisk OR an ampersand (&)
ampersand = input("Enter an ampersand please")
    if ampersand == "&":
        print("good!")
    else:
        print("not ampersand :(")
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
Integer= input("enter a integer")
if Integer.isdigit():
    Integer= int(Integer)
else:
    print("incorrect")
print("correct")
    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
Input1 = input("type in marist")

if "marist" in Input1:
    print("it does have the substring marist.")
else:
    print("does not have the sub string marist.")
main()
