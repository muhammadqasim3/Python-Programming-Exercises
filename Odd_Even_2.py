number = int(input("Enter the number you want to check: "))
if number % 2 == 0 and number % 4 == 0:
    print("Even and Divisible by 4")
elif number % 2 == 0:
    print("Even")
else:
    print("odd")
