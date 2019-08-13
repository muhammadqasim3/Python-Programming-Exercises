# There are various solutions to this problem.
user_input = input("Enter any sentence: ")


def reverse_word():
    reversed_input = user_input.split()
    return " ".join(reversed_input[::-1])


print(reverse_word())