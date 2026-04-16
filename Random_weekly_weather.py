import random

weather = []
for i in range(7):
    temp = random.randint(20, 43)
    weather.append(temp)
print("7 day weather forcast", weather)

hottest_temp = 0
for day in weather:
    if day > hottest_temp:
        hottest_temp = day
print(f"Hottest temp is {hottest_temp}")

for day in weather:
    if hottest_temp >= 40:
        print("Warning: Extreme Heatwave!")
        break
    elif hottest_temp >= 30:
        print("Forecast: Normal Summer Weather.")
        break
    else:
        print("Forecast: A surprisingly cool week.")
        break
