import random

history = []
days = int(input("How many days? "))

for d in range(1, days + 1):
    weather = ["Sunny", "Rainy", "Snowy"][random.randrange(3)]
    temp = random.randrange(-10, 41)

    if temp < 5:
        clothes = "Heavy coat"
    elif temp < 15:
        clothes = "Jacket"
    elif temp < 25:
        clothes = "Sweater"
    else:
        clothes = "T-shirt"

    print("Day", d, "-", weather, "-", temp, "C -", clothes)
    history.append(weather)

print("History:", history)
