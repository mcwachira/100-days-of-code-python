import string
from art import logo
print(logo)

letters = list(string.ascii_lowercase)



def caesar(message, shift, direction):
    result = ''

    # normalize shift (handles large numbers)
    shift =shift % 26

    if direction == "decode":
        shift*=-1

    for char in message:
        if char in letters:
            index = letters.index(char)
            new_index = (index + shift) % 26
            result += letters[new_index]
        else:
            result+=char

    return result


def menu():
    print("\n===== Caesar Cipher Tool =====")
    print("1. Encode message")
    print("2. Decode message")
    print("3. Exit")

use_again = True

while use_again:
    menu()
    choice = input("Choose an option (1/2/3): ")

    if choice == "3":
        print("Goodbye ")
        break

    if choice not in ["1", "2"]:
        print("Invalid choice. Try again.")
        continue

    message = input("Enter your message: ").lower()

    try:
        shift = int(input("Enter shift number: "))
    except ValueError:
        print("Shift must be a number!")
        continue

    if choice == "1":
        result = caesar(message, shift, "encode")
        print(f"Encoded message: {result}")

    elif choice == "2":
        result = caesar(message, shift, "decode")
        print(f"Decoded message: {result}")

    again = input("\nDo you want to continue? (y/n): ").lower()
    if again != "y":
        use_again = False
        print("Thanks for using the tool ")