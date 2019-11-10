import random
word = input("enter a word : ")
shuffled = list(word)
random.shuffle(shuffled)
shuffled = '\n'.join(shuffled)
shuffled = shuffled.upper()
print(shuffled)
