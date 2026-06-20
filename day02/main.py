print ("Welcome to the tip calculator!")
bill = float(input('What was the total bill ? $'))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people_split_bill = int(input("How many people  to split the bill ?"))

bill_with_tip = (bill + (tip/100 * bill))
split = bill_with_tip/people_split_bill
print(f"Each person should pay: ${round(split,2)}")