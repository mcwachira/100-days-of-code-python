from art import logo
print(logo)
print("Welcome to the private bidding auction")

bidders = {}
user_count  = 1

highest_bid = 0
winner = ""


use_again = True


while use_again:
    name = input("What is your name?:")
    bid = input("How Much would you like to bid?:")

    unique_key = f"user_{user_count}"
    bidders[unique_key] = {}


    bidders[unique_key]["name"] = name
    bidders[unique_key]["bid"] = bid

    print(bidders)

    for value in bidders:
        if int(bidders[value]["bid"]) > highest_bid:
            highest_bid = int(bidders[value]["bid"])
            winner = bidders[value]['name']

    user_count+=1


    again = input('Are there other bidders for this auction? Type "yes" or "no" ')
    if again != "yes":
        use_again = False
        print(f"The winner is {winner} with a bid of {largest_number}")