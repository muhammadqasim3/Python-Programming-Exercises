from random import randint

number = randint(1, 9)
guess = 0
count = 0
print(number)
while guess != number and guess != 'exit':
    guess = int(input("Guess the number: "))
    count += 1
    if guess < number:
        print("Low!")
    elif guess > number:
        print("High!")
    else:
        print("Correct! You got it.")
        print("It takes you " + str(count) + " attempt/s to guess correct number.")

