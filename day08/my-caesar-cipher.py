import string
from art import logo

print(logo)

letters = list(string.ascii_lowercase)


def encrypt(message, shift):
    positions = []
    new_positions = []
    new_message = []

    for i in message:
        index = letters.index(i)
        # print(index)
        positions.append(index)
    # print(positions)
    for position in positions:
        new_index = position + shift

        if new_index >= len(letters):
            new_index = shift - (len(letters) - position)
            # print(new_index)
            new_positions.append(new_index)

        else:
            new_positions.append(new_index)
    # print(new_positions)

    for i in new_positions:
        new_message.append(letters[i])

    encoded_message = "".join(new_message)
    # print(encoded_message)

    return encoded_message


def decrypt(message, shift):
    positions = []
    new_positions = []
    new_message = []

    for i in message:
        index = letters.index(i)
        # print(index)
        positions.append(index)
    # print(positions)
    for position in positions:
        new_index = position - shift
        new_positions.append(new_index)
    # print(new_positions)

    for i in new_positions:
        new_message.append(letters[i])
    decoded_message = "".join(new_message)
    # print(decoded_message)

    return decoded_message


use_again = True

while use_again:
    choice = input('Type "encode" to encrypt , type "decode" to decrypt').lower()

    if choice not in ["encode", "decode"]:
        print('Type "encode" to encrypt , type "decode" to decrypt')
        continue

    message = input("Type Your Message :")
    if not message.isalpha():
        print('Please enter strings only')
        continue

    shift = int(input("Type the shift number :"))

    if (choice == "encode"):
        result = encrypt(message, shift)
        print(result)

    elif (choice == "decode"):
        result = decrypt(message, shift)
        print(result)

    # -------- Play Again --------
    again = input("Use again? (y/n): ").lower()
    if again != 'y':
        use_again = False
