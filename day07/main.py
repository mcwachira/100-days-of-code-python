import random

words_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(words_list)
print (chosen_word)
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

guessed_letters = []

while placeholder != chosen_word:
    guess = input("Guess a letter\n").lower()

    print(guess)
    guessed_letters.append(guess)
    display = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)

    placeholder = display

print("You got it !",placeholder)