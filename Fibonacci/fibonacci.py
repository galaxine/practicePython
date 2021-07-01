# fibonacci is basically result_n = result_n-1 + result_n-2
def fuckonacci(number):
    list = []
    for i in range(1,number + 1):
        if i <= 2:
            list.append(1)
        else:
            fib_n_minus_1 = list[len(list)-2]
            fib_n_minus_2 = list[len(list)-1]
            list.append(fib_n_minus_1 + fib_n_minus_2)
    print(list)    


amount = input("Enter how many fibonacci numbers you want\n")
if amount.isnumeric:
    fuckonacci(int(amount)) 
else:
    print("you didn't enter a number")

