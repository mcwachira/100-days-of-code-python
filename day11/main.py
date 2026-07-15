import random
from art import logo
print(logo)

# Creat a deck of cards
def create_deck():
    # 4 sets of cards (like 4 suits)
    return [11,2,3,4,5,6,7,8,9,10,10,10,10]*4

# deal one card

def deal_card(deck):
    # Remove and return the top card from the deck
    return deck.pop()

# calculate score
def calculateScore(cards):
    total = sum(cards)
    while total> 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

        total = sum(cards)
    return total


# players turn to play
def player_turn(deck, player_cards):
    while True:
        player_score = calculateScore(player_cards)
        print(f"\nYour cards: {player_cards} | Score: {player_score}")

        #check if player won or lost
        if (player_score > 21):
            print("You went over 21. You lose!")
            return player_score
        elif (player_score == 21):
            print("Blackjack! You win!")
            return player_score

        # Ask for input
        choice = input("Type 'y' to hit or 'n' to stand: ").lower()

        if choice == 'y':
            # Draw a new card
            new_card = deal_card(deck)
            player_cards.append(new_card)
            print(f"You drew: {new_card}")
        elif choice == 'n':
            # End player turn
            return player_score
        else:
            print("Invalid input. Try again.")



# dealers turn
def dealer_turn(deck, dealer_cards):
    print(f"\nDealer's cards: {dealer_cards}")

    #Dealer must draw until the reach at least 17
    while calculateScore(dealer_cards) < 17:
        new_card = deal_card(deck)
        dealer_cards.append(new_card)
        print(f"Dealer drew: {new_card}")

    dealer_score = calculateScore(dealer_cards)
    print(f"Dealer's final hand: {dealer_cards} | Score: {dealer_score}")
    return dealer_score




# compare scores
def compare_scores(player_score, dealer_score):
    if player_score > 21:
        print("You lose!")
    elif dealer_score > 21:
        print("Dealer went over. You win!")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("You lose!")
    else:
        print("It's a draw!")


# play one game

def play_game():
    #create and shuffle the  dec
    deck = create_deck()
    random.shuffle(deck)

    # Deal initial hands
    player_cards= [deal_card(deck), deal_card(deck)]
    dealer_cards = [deal_card(deck), deal_card(deck)]

    # Show initial cards (hide dealer second card)
    print(f"\nYour cards: {player_cards}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    # Player turn
    player_score = player_turn(deck, player_cards)
    #Dealer turn ONLY if player didn't bust or hit blackjack
    if player_score <= 21 and player_score != 21:
        dealer_score = dealer_turn(deck, dealer_cards)
    else: dealer_score = calculateScore(dealer_cards)
    # Compare final scores
    compare_scores(player_score, dealer_score)



#MAIN GAME LOOP

while True:
    start = input("\nDo you want to play Blackjack? (y/n): ").lower()

    if start == 'y':
        play_game()
    elif start == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Try again.")