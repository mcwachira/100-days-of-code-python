import random

from art import logo
print(logo)

#generate random number
def generate_random_number():
    # Returns a random number between 1 and 100
    return random.randint(1, 100)


#generate difficulty
def set_difficulty():
    #enter difficulty
    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
    if(difficulty == "easy"):
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number")
        return attempts
    elif(difficulty == "medium"):
        attempts = 7
        print(f"You have {attempts} attempts remaining to guess the number")
        return attempts
    elif(difficulty == "hard"):
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number")
        return attempts
    else:
        print("Invalid input. Please choose easy, medium, or hard.")

# Function: Get user guess
def get_guess():
    while True:
        try:
            guess = int(input("Guess the number: "))
            # Validate range
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


#check Guess

def check_guess(guess, number):

    if guess > number:
        print("Guessed Number is to high")
        return False
    elif guess < number:
        print("Guessed Number is to low")
        return False
    elif guess == number:
        print("You guessed the Correct Number")
        return True


# MAIN GAME LOOP

play_again = True
while play_again:
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    #setup Game
    number = generate_random_number()
    attempts = set_difficulty()

    #Game loop
    while attempts > 0:
        guess = get_guess()

        # Check result
        is_correct = check_guess(guess, number)

        if is_correct:
            break  # exit loop if user wins

        #reduce attempts if wrong
        attempts-=1
        print(f"Attempts remaining: {attempts}")

    #if attempts run out
    if attempts == 0:
        print(f"You are out of attempts . The number was {number}!")

        # Replay option
    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        play_again = False
        print("Thanks for playing!")
