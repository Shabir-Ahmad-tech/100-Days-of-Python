# Day 2; Tip Calculator
print("-------Welcome to the Tip calculator--------")
Total_bill = float(input("What was your total bill? $"))
Tip = float(input("How much percent tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people are you? "))

Total_bill_with_tip = Total_bill + (Total_bill * Tip / 100)
bill_per_person = Total_bill_with_tip / people
print(f"Each person should pay: ${round(bill_per_person, 2)}")





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# print(type(2))
# print(type("Shabir Ahmad"))
# print(type(1.242))
# print(type(True))

# print(str(123) + str(321))

# # print("The number of letters in your name is: " + str(len(input("what is your name: "))))

# print(1 + 2)
# print(2 - 1)
# print(2 * 2)
# print(5 / 2)
# print(5 // 2)
# print(2 ** 2)
# print(5 % 2)

# # PEMDAS
# print(3 * 4 - 5 + 2 / 4 * 2 - 2 + 1 ** 2)
# print(3 * 3 + 3 / 3 - 3)

# #BMI
# # height = input("enter your height in m: ")
# # weight = input("enter your weight in kg: ")

# # BMI = float(weight) / float(height) ** 2
# # print(BMI)
# # print(round(BMI, 2))

# print(round(3.634224, 3))

# name = input("Enter your name: ")
# print(f"Hello, {name}")
# print("Hello " + name)
