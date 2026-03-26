# Day 2; Tip Calculator
#========================================
# Explanation of this project:
# This project is a simple tip calculator 
# that takes the user's total bill and tip percentage as input and outputs the total bill with tip.
#========================================


print("-------Welcome to the Tip calculator--------")
Total_bill = float(input("What was your total bill? $"))
Tip = float(input("How much percent tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people are you? "))

Total_bill_with_tip = Total_bill + (Total_bill * Tip / 100)
bill_per_person = Total_bill_with_tip / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

