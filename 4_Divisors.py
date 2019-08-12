num_list = []
for i in range(2, 11):
    num_list.append(i)

print(num_list)

user_input = int(input("Enter any number you want to check: "))

for num in num_list:
    if num % user_input == 0:
        print("Divisor of ", num)
