from art import logo, vs
from game_data import data
import random
print(logo)

#generate a random choice
def generate_random_value():
    choice= random.choice(data)
    # print(choice)
    return choice

def format_data(value):
        #Format value for display
    return f"{value['name']}, a {value['description']} from {value['country']}"


def get_user_choice():
    while True:
        choice = input("Who has more followers? Type 'A' or 'B' ").upper()
        if choice in ["A", "B"]:
            return choice

        print("Invalid input. Please type 'A' or 'B'.")

def check_answer(choice, first_value, second_value,score):

    first_follower_count = first_value["follower_count"]
    second_follower_count = second_value["follower_count"]
    if first_follower_count > second_follower_count:
        correct_answer = "A"
    else:
        correct_answer = "B"
        # Compare the values based on what's Selected
    if correct_answer == choice:
        score += 1
        print(f"You are right! Current score: {score}")
        return {"game_over": False, "score": score}
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return {"game_over": True, "score": score}


# MAIN GAME LOOP

play_again = True
game_over = False
while play_again:

    #Reset Game
    score = 0
    game_over = False

    #Initial Values
    first_value = generate_random_value()
    second_value = generate_random_value()


    #check and ensure first and second value are not the same
    while first_value == second_value:
        second_value = generate_random_value()
    #Game loop
    while game_over  != True :

        print(f"\nCompare A: {format_data(first_value)}")
        print(vs)
        print(f"Against B: {format_data(second_value)}")

        # Get user input
        user_choice = get_user_choice()
        # Check result
        result = check_answer(user_choice, first_value, second_value, score)

        score = result["score"]

        if result["game_over"]:
            game_over = True
        else:
            # shift second value to first value for the next round
            first_value = second_value
            second_value = generate_random_value()

            #Ensure the new generated second value is not the same as the first value
            while first_value == second_value:
                second_value = generate_random_value()



        # Replay optiongenerate_random_value()
    again = input("Do you want to play again? (y/n): ").lower()
    game_over = False
    if again != 'y':
        play_again = False
        game_over = True
        print("Thanks for playing!")