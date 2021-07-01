"""
In order to check the primality of a number, the number needs to be prime:
So it needs to be divisable by itself and one only
1,2,3,5,7, etc. can only be divided by 1 or itself.
in order to find the number"""

print("Enter a number and we will see if it is a prime or not")
print("Enter the number: ")

def checkForPrime(number: int):
    primelist: list[int] = []
    usedList: list[int] = []
    for i in range(1,number+1):
        usedList.append(i)
        if number % i == 0:
            primelist.append(i)
    if len(primelist) == 2:
        print("This number is prime, take a look")
        print(primelist)
    else:
        print("The number is not prime, look how many more divisors it has:")

number: str = input()
if number.isnumeric():
    checkForPrime(int(number))
else:
    print("did you realy enter a number?")

