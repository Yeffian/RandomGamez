import random

running = True

print('Welcome to the Guessing Game!')
difficulty = input('Do you want to play on Easy, Medium or Hard? ')

number = 0

if difficulty.lower() == 'easy':
    number = random.randint(0, 10)
elif difficulty.lower() == 'medium':
    number = random.randint(0, 15)
elif difficulty.lower() == 'hard':
    number = random.randint(0, 100)
else:
    print('Invalid, try again')


while running:
    guess = int(input('Enter your choice: '))

    if guess == number:
        print('Congrats, you got it!')
        running = False
    elif guess > number:
        print('Too high, try again')
    elif guess < number:
        print('Too low, try again')