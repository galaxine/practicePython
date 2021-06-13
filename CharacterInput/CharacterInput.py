# Create a program that asks the user to enter their name and their age
# Print a message addressed to them how long they have to lie until hundred
# EXTRAS:
#   1. Add a function to ask them another number and then print the number of the presvious message
#   2. Print out that many copies of the previous message on seperate lines


def askUserName() -> str:
    print("Please tell me your name and your age:")
    print("Name: ")
    name: str = input()
    return name


def askUserAge() -> int:
    print("Age: ")
    age: int = int(input())
    return age


def messageToUserAndRemainingTime(name: str, age: int) -> str:
    oldAge: int = 100
    message: str = f"Hello {name}, you have {oldAge - age} years left to become 100 years old."
    return message


def repeatMessage(message: str) -> None:
    print("How often do you want to repeat the message?")
    times: int = int(input())
    print("'same' line or 'diff'erent lines or 'trad'itional new lines?")
    command: str = input()
    if command == 'same':
        for i in range(0, times):
            print(message, end=" ")
    elif command == 'diff':
        for i in range(0, times):
            for e in message:
                print(e)
    elif command == 'trad':
        for i in range(0, times):
            print(message)


message: str = messageToUserAndRemainingTime(askUserName(), askUserAge())
print(message)
repeatMessage(message)
