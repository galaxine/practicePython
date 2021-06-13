def checkDivisors(num: int, check: int):
    x = range(2, num)
    for e in x:
        if e % check == 0:
            print(e)

checkDivisors(477, 13)
