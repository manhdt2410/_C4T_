from turtle import *
import random
shape("turtle")
n = int(input("so canh cua da giac deu la "))
a = ['green','blue','red','yellow'] # _colorful polygon!!!_
speed(31000)
i = int(0)
while i < n:
  color(a[random.randint(0, 3)]);
  forward(100)
  left(360.0/n)
  i = i + 1
mainloop()
