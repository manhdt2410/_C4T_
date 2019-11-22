from turtle import *
import random
shape("turtle")
speed(2)
colors_list = ["blue", "red", "teal", "green", "gray"]
for i in range(10) :    
    color(random.choices(colors_list))
    forward(30)

mainloop()
