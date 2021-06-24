# palindrome is checked by size or also exercise 6


def is_palindrome(string: str) -> bool:
    if len(string)%2 == 0:
        first_half: str = string[0:int(len(string)/2)]
        second_half: str = string[int((len(string)/2)):(len(string))]
        if first_half == second_half[::-1]:
            return True
        else:
            return False
    if len(string) % 2 == 1:
        first_half: str = string[0:int(len(string)/2-0.5)]
        second_half: str = string[int(len(string)/2+0.5):len(string)]
        if first_half == second_half[::-1]:
            return True
        else:
            return False



print(is_palindrome("asksam"))