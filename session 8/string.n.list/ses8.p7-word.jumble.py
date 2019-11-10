import random
this_tuple = ('dog', 'cat', 'mouse', 'home')
ans = ('dog', 'cat', 'mouse', 'home')
word = random.choice(this_tuple)
shuffled = list(word)
random.shuffle(shuffled)
shuffled = ' '.join(shuffled)
print(shuffled) 
ans = input("your answer : ")
if ans == word:
    print("original word : ",word)
    print("correct!")
else :
    print("original word : ",word)
    print("wrong!")

