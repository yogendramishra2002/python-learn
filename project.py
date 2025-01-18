import random
target = random.randint(1,100)

# def guess_game():

while True:
    guess = int(input("Enter your guess: "))
    if guess == target:
        print("You have guessed it right!")
        break
    elif guess < target:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
        
print("...Game Over...")


    