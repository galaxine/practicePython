import random as rand

the_number = rand.randint(1,9)
print("guess the number: ")
while True:
    number: str = input()
#    assert int(number) and 0 < int(the_number) < 10, "Enter a number and it has to be between 1 and 9"
    if number.isnumeric() and 0 < int(number) < 10:
        if int(number) == the_number:
            print("you won!")
            break
        elif int(number) > the_number:
           print("too high")
        elif int(number) < the_number:
            print("too low")
    else:
        print("enter a number, between 1 and 9")