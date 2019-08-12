print("*************PRIME Checker**************")
number = int(input("Enter the number: "))
if number == 1 or number == 2:
    print("Prime!")
elif number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Not Prime!")
            print(i, " times ", number//i, " is ", number)
            break
        else:
            print("Prime!")
