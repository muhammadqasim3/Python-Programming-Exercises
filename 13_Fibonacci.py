print("*****************Fibonacci Series******************")



def fabonacci():
    user_input = int(input("How many numbers do you want to generate ? : "))
    i = 1
    fib = []
    if user_input == 0:
        fib = []
    elif user_input == 1:
        fib = [1]
    elif user_input == 2:
        fib = [1, 1]
    elif user_input > 2:
        fib = [1, 1]
        while i < (user_input - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

print(fabonacci())

