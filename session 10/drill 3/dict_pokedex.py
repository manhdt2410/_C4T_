pokedex = {
    "raichu" : '''raichu has a regional variant that is Electric/Psychic. It evolves from Pikachu when exposed to a Thunder Stone.
All Pikachu in Alola will evolve into this form regardless of their origin.''',
    "onix" : '''Onix resembles a giant chain of gray boulders that become smaller towards the tail. 
It has a rocky spine on its head and a pair of black eyes right beneath it.This Pokémon has a magnet
in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body
very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to 
black diamonds.''',
    "jirachi" : "legendary pokemon!, unknown information...",
    "moi" : "mytical creature!!!!"
}
while True:
    ans = input("Enter pokemon name : ")
    ans = ans.lower()
    if ans == "raichu":
        print(pokedex["raichu"])
    elif ans == "onix":
        print(pokedex["onix"])
    elif ans == "jirachi":
        print(pokedex["jirachi"])
    elif ans == "moi":
        print(pokedex["moi"])
    elif ans == "stop":
        print("stop searching!")
        break
    else:
        print("pokedex not found!")
