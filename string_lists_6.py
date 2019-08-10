print("**************PPALINDROME****************")
user_input = input("Enter a string: ")
inverse_input = user_input[::-1]

if user_input == inverse_input:
    print(user_input + " is a Palindrome")
else:
    print(user_input + " is not a Palindrome")

