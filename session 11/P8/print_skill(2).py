
a = {
    "name" : "tackle",
    "min lv" : 1,
    "damage" : 5,
    "hit rate" : 0.3,
}
b = {
    "name" : "quick atk",
    "min lv" : 2,
    "damege" : 3,
    "hit rate" : 0.5,
}
c = {
    "name" : "strong kick",
    "min lv" : 4,
    "damege" : 9,
    "hit rate" : 0.2,
}
print('skills : ')
skills = [a["name"], b["name"], c["name"]]
for m,n in enumerate(skills):
    print(m + 1, n, sep='. ')