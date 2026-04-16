import random

weather = []
for i in range(7):
    temp = random.randint(20, 45)
    weather.append(temp)
print("7 day weather forcast", weather)

hottest_temp = 0
for day in weather:
    if day > hottest_temp:
        hottest_temp = day
print(f"Hottest temp is {hottest_temp}")

for day in weather:
    if day > 40:
        print("Warning! Heat wave expected!")
        break
