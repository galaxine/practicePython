# Ask the user for a number
# react by mod 2
#   also react if it's mod 4
#
#   aks the use for two numbers, the number and the mod
#


def checkIfModByTwo() -> int:
    print("Enter a number so we can see if it is divisable by 2:")
    number: int = int(input())
    if number % 2 == 0:
        print("The number is divisable by 2 and is even")
        return number
    else:
        print("The number is odd and not divisable by 4")
        return number


def checkIfDivisibleByFour(number: int) -> None:
    print("Let's check if the number is divisable by 4 too")
    if number % 4 == 0:
        print("The number is divisable by 4, too")
    else:
        print("not divisable by 4")

def checkIfNIsDivisableByM(num: int, check: int):
    if num % check == 0:
        print("divisable by the check")
    else:
        print("non divisable by check")


checkIfDivisibleByFour(checkIfModByTwo())
checkIfNIsDivisableByM(10, 2)

