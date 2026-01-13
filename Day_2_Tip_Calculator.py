# Day 2; Tip Calculator
print("-------Welcome to the Tip calculator--------")
Total_bill = float(input("What was your total bill? $"))
Tip = float(input("How much percent tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people are you? "))

Total_bill_with_tip = Total_bill + (Total_bill * Tip / 100)
bill_per_person = Total_bill_with_tip / people
print(f"Each person should pay: ${round(bill_per_person, 2)}")

