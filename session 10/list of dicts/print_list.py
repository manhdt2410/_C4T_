import math
p1 = {
    "name" : "Huy",
    "role" : "waiter",
    "hours" : 12,
    "salary per our($)" : 0.8,
}
p2 = {
    "name" : "Tung",
    "role" : "cook",
    "hours" : 24,
    "salary per our($)" : 1.5,
}
p3 = {
    "name" : "M.Duc",
    "role" : "manager",
    "hours" : 20,
    "salary per our($)" : 2.0,
}
p4 = {
    "name" : "Don",
    "role" : "waiter",
    "hours" : 12,
    "salary per our($)" : 0.9,
}
p5 = {
    "name" : "H.Duc",
    "role" : "waiter",
    "hours" : 14,
    "salary per our($)" : 0.7,
}

table = [p1, p2, p3, p4, p5]
m1 = [p1["hours"], p1["salary per our($)"]]
m2 = [p2["hours"], p2["salary per our($)"]]
m3 = [p3["hours"], p3["salary per our($)"]]
m4 = [p4["hours"], p4["salary per our($)"]]
m5 = [p5["hours"], p5["salary per our($)"]]
money = [m1, m2, m3, m4, m5]
for i in money:
    print(i)
