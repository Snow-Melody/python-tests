import random

def guess_my_number():
    guess_my_number = random.randint(1, 666)
    guess = None 
    attempts = 0

    print("I would like to play a game!")
    print("I'm thinking of a number between 1 and 666. If you choose wrong you are banished.")

    while guess != guess_my_number:
        guess = int(input("Go ahead and guess: "))
        attempts += 1

        if guess < guess_my_number:
            print("guess too low! Banished!")
        elif guess > guess_my_number:
            print("Guess too high! Banished!")
        else:
            print(f"Congratulations you guessed correctly in {attempts} attempts! Not banished!")

            guess_my_number()