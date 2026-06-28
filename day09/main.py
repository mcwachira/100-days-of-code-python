import platform
import os
from art import logo
print(logo)
print("Welcome to the private bidding auction")

def clear_screen():
    # Detect the operating system
    current_os = platform.system()

    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_valid_bid():
    while True:
        bid = input("How Much would you like to bid?:")
        if(bid.isdigit()):
            return int(bid)
        else:
            print('enter a valid number')







play_again = True
while play_again:

    bidders = {}
    user_count = 1
    use_again = True

    while use_again:
        name = input("What is your name?:")
        bid = get_valid_bid()

        unique_key = f"user_{user_count}"
        bidders[unique_key] = {}
        bidders[unique_key]["name"] = name
        bidders[unique_key]["bid"] = bid

        clear_screen()

        again = input('Are there other bidders for this auction? Type "yes" or "no" ')
        if again != "yes":
            use_again = False
        user_count += 1

        # -------- Find Winner --------
        highest_bid = 0
        winner = ""
        for user in bidders:
            if int(bidders[user]["bid"]) > highest_bid:
                highest_bid = int(bidders[user]["bid"])
                winner = bidders[user]['name']

        print(f"The winner is {winner} with a bid of {highest_bid}")

        # -------- Play Again --------
        again = input("Do you want to run another auction? (yes/no): ").lower()
        if again != "yes":
            play_again = False
            print("Thanks for using the auction program!")