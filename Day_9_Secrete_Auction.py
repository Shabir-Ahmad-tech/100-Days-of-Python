# Day 9: Silent Auction
#========================================
# Explanation of this project:
# This project is a simple function that finds the highest bidder in a silent auction and outputs the result.
#========================================


Bid = {'name': 0 , 'bid': 0}
while True:
    name = input("Enter your name: ")
    bid_amount = float(input("What is your bid amount?: "))
    Bid[name] = bid_amount
    again = input("Do you want to continue? (yes/no):").lower()
    if again == 'yes' or again == 'y':
        continue
    elif again == 'no' or again == 'n':
        break
    else:
        print("Invalid input")

highest_bid = 0
winner = ''
for key in Bid:
    if Bid[key] > highest_bid:
        highest_bid = Bid[key]
        winner = key
print(f"Winner is {winner} with a bid of {highest_bid}")




# programming_Dict = {
#     'Bug':'An error in a computer program',
#     'Function':'A reusable block of code that performs a specific task',
#     'Variable':'A container for storing data values',
#     'Loop':'A control structure that repeats a block of code multiple times',
#     'Condition':'A statement that evaluates to either True or False'
# }

# programming_Dict['Bug'] = 'A flaw in a computer program that causes it to produce incorrect results'

# print(programming_Dict['Bug'])

# for key in programming_Dict:
#     print(key)
#     print(programming_Dict[key])

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,}

# for key in student_scores:
#     if student_scores[key] >= 90:
#         student_grades[key] = 'Outstanding'
#     elif student_scores[key] >= 80:
#         student_grades[key] = 'Exceeds Expectations'
#     elif student_scores[key] >= 70:
#         student_grades[key] = 'Acceptable'
#     else:
#         student_grades[key] = 'Fail'

# print(student_grades)

# travel_log = {
#     'Pakistan' : ['Swat', 'Lahore', 'Islamabad'],
#     'Turkiye' : ['Istanbul', 'Ankara', 'Izmir'],
#     'Korea': {
#         'North Korea': ['Pyongyang', 'Hamhung'],
#         'South Korea':['Seoul', 'Busan']
#     }
# }

# print(travel_log['Korea']['North Korea'][0])

# just = ['A', 'B', ['C', 'D']]
# print(just[2][1])

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }


# starting_dictionary['c'] = 7
# final_dictionary = starting_dictionary
# print(final_dictionary)
