import random as rand

the_number = rand.randint(1,9)
print("guess the number: ")

c: int = 0
while True:
    number: str = input()
#    assert int(number) and 0 < int(the_number) < 10, "Enter a number and it has to be between 1 and 9"
    if number.isnumeric() and 0 < int(number) < 10:
        if int(number) == the_number:
            print("you won! And it only took you " + str(c) + " tries")
            break
        elif int(number) > the_number:
            c += 1
            print("too high")
        elif int(number) < the_number:
            c += 1
            print("too low")
    elif the_number == "exit":
        print("bye then")
        break
    else:
        print("enter a number between 1 and 9, dork")