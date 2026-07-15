import random
from art import logo
print(logo)



def dealCards():
    # Card values (Ace = 11 for now)
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card  = random.choice(cards)
    return card

def calculateScore(cards):
    total = sum(cards)
    while total> 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

        total = sum(cards)
    return total

play_again = True
while play_again:

    player_cards = []
    pc_cards = []

    # Ask player if they want to start
    value = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if value == 'y':

        #deal 2 cards to the player and pc at the same time
        for _ in range(2):
            player_cards.append(dealCards())
            pc_cards.append(dealCards())

        print(f"Your cards :{player_cards}")
        print(f"Pc first cards :{pc_cards[0]}")

        # ---------------- PLAYER TURN ----------------
        player_turn = True

        while player_turn:
            player_score =sum(player_cards)
            if(sum(player_cards) > 21):
                print("You went over 21. You lose!")
                break
            elif(sum(player_cards) == 21):
                print("Blackjack! You win!")
                break

            # Ask player if they want another card
            value = input("Do you want to get another card? Type 'y' or 'n':").lower()
            if value == 'y':

                # add one new card
                new_card = dealCards()
                player_cards.append(new_card)
                print(f"You drew: {new_card}")
                print(f"Your cards: {player_cards}")

            else:
                #players turn is false
                player_turn = False

            # ---------------- DEALER TURN ----------------
            # Only run if player didn't bust

                if(sum(player_cards) <21):
                    print(f"\nComputer's cards: {pc_cards}")
                #dealer must draw until reaching 17 or higher

                    while sum(pc_cards) <17 :
                        new_card = dealCards()
                        pc_cards.append(new_card)

                        print(f"Computer draws: {new_card}")

                    print(f"Computer's final hand: {pc_cards}")

                    # ---------------- RESULT ----------------
                    player_score =calculateScore(player_cards)
                    pc_score = calculateScore(pc_cards)

                    if pc_score > 21:
                        print("Computer went over 21. You win!")
                    elif player_score > pc_score:
                        print("You win!")
                    elif player_score < pc_score:
                        print("You lose!")
                    else:
                        print("It's a draw!")


    elif value == 'n':

        # Exit immediately if player doesn't want to start

        break

        # ---------------- PLAY AGAIN ----------------

    again = input("\nDo you want to play again? (y/n): ").lower()

    if again != "y":
        play_again = False

        print("Thanks for playing blackjack!")