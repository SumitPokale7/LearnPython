print(f"Welcome to the tip calculator!")

bill   = float(input("What was the total bill?\n"))
tip    = int(input("How much tip would you like to give? 10%, 12% Or 15%?\n"))
people = int(input("How many people to split the bill?\n"))

tip_as_percent   = tip / 100
total_tip_amount = bill * tip_as_percent
totalBill        = bill + total_tip_amount
bill_per_person  = totalBill / people
finalAmount      = round(bill_per_person, 2)

print("Each person should pay:", finalAmount)