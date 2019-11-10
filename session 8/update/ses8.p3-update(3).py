favourite_films = ['Tom and Jerry', 'Mickey mouse', 'Batman', 'Thor']
print(favourite_films)
i = int(input("choose a number? "))
if -4 < i < 4 :
    favourite_films[i] = input("enter your favourite film? ")
    print(favourite_films)
else:
    print("invalid number")
