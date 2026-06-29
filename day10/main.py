from art import logo
print(logo)

#add
def add(n1, n2):
    return n1 +n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 *n2

#divide
def divide(n1, n2):
    return n1/n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

result = None
go_again = True
while go_again:

    #Get First Number
    if result == None:
        first_number = float(input("What is the first Number?:"))
    else:
        first_number = result

    # Show Math Operations
    print("+\n-\n*\n/\n")

    #Get Math operation
    operation = input("Type a math operation:")
    if(operation not in operations):
        print("Please use a valid operation")
        continue

    #Get Second Number
    second_number = float(input("What is the next Number ?:"))

    # Division check
    if(operation == "/" and   second_number == 0):
        print("Number cannot be divided by zero")
        continue

    # Perform calculation
    result = operations[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} ={result}")

    again = input(f'type "y" to continue with calculating {result}, type "n" to exit or type "new" for a brand new calculation')

    if again == 'y':
        continue
    elif again == "new":
        result = None
    elif again == "n":
        go_again = False
        print("Thanks for using the calculator!")
    else:
        print("Invalid input. Exiting.")
        go_again = False