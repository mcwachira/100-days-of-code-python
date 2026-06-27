import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo3


print (logo3)
score = 0
play_again = True

while play_again:
    # -------- Difficulty Input Validation --------#
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        else: print("Invalid input. Please choose easy, medium, or hard.")

    # -------- Setup --------#
    chosen_word = random.choice(word_list)
    # print(chosen_word)
    placeholder = ""
    for position in range(len(chosen_word)):
        placeholder += "_"
    print(placeholder)

    guessed_letters = []
    game_over = False
    score_bonus = 0
    lives = 0
    if difficulty == 'easy':
        lives = 10
        score_bonus  =5
    elif difficulty == 'medium':
        lives = 6
        score_bonus = 10
    elif difficulty == 'hard':
        lives = 4
        score_bonus =15

    while not game_over :
        print(f"*********************************************{lives} Lives Left **********************************************")
        guess = input("Guess a letter\n").lower()

        # -------- Input Validation (single letter) --------#

        if len(guess)!=1 or not guess.isalpha():
            print("Please Enter a Single Valid Letter")
            continue

        print(guess)
        if guess in guessed_letters:
            print(f"You already guessed that letter {guess}")
            continue

        guessed_letters.append(guess)
        display = ""

        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter

            else:
                display += "_"


                # print(stages[lives])

        print(display)
        if(guess not in chosen_word):
            print(f"You  guessed {guess} that not in the chosen word ")
            lives = lives - 1

            if lives == 0:
                game_over = True
                print('Game Over You Lose')
        else:
            score += 1


        if(display == chosen_word):
            score = score +score_bonus
            print("You got it !", display)
            print ("Your Total Score", score)
            game_over = True

        print(stages[lives])

# -------- Play Again --------
again = input("Play again? (y/n): ").lower()
if again != 'y':
    play_again = False

print("Thanks for playing! Final score:", score)