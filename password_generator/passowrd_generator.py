# Password generator: we can do this by relying on
# the length of the password and the types of characters being used.
import random as r
numbers = "1234567890"
alphabet = "abcdefghijklmnopqrstuvwxyz"
special = "!\"§$%&/()=?`´\\][}{><|-_.:,;#'"

# get an input how long it needs to be, turn it into an int
# 
# Randomly choose one of the three list
# then choose randomly by the length of the list.
#   if it is alphabet, flip a coin if it is upper or lowercase

def chooseList()-> str:
    num = r.randrange(0,3)
    if num == 0:
        return numbers
    elif num == 1:
        return lower_or_upper()
    elif num == 2:
        return special
    else:
        return "error in chooseList"

def lower_or_upper()-> str:
    num = r.randrange(0,2)
    if num == 0:
        return alphabet.upper()
    elif num == 1:
        return alphabet
    return "error in lower_or_upper"

def return_element(list)-> str:
    num = r.randrange(0, len(list))
    return list[num]

def create_strong_password(num: int)-> str:
    password = ""
    for i in range(0,num+1):
        password += return_element(chooseList())
    return password


num = input("Enter the length of your password:\n>>>")
password = create_strong_password(int(num))
print(password)
