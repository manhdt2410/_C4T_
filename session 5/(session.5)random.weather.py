import random
random = random.randint(0,100)
print(random)
if random < 30:
    print("rainy")
elif random < 60:
    print("cloudy")
else:
    print("sunny")
