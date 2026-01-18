# Day 5: Password Generator
#========================================
# Explanation of this project:
# This project is a simple password generator 
# that takes the user's choices as input and outputs the result.
#========================================
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print("----Welcome to the Password generator----")
nu_char = int(input("Enter how many characters would you like in your password: "))
nu_numbers = int(input("Enter how many numbers would you like in your password: "))
nu_symbols = int(input("Enter how many symbols would you like in your password: "))

password = []
for char in range(nu_char):
    password.append(random.choice(letters))
for char in range(nu_numbers):
    password.append(random.choice(numbers))
for char in range(nu_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
print(password)

# #==========================
# #----Code Challenge 01-----
# #==========================
# #numbers in 200 random
# students = [149, 176, 172, 56, 97, 155, 185, 183, 167, 156, 145, 132, 123, 112, 101, 90, 89, 78, 67]

# max_score = 0
# for student in students:
#     if student > max_score:
#         max_score = student     
# print("Max score is:",max_score)

# #==========================
# #----Code Challenge 02-----
# #==========================

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)