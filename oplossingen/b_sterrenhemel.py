import random
import turtle
from sterren_module import *

kleuren = ("red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat")

for _ in range(30):
    x_positie = random.randint(-350, 350)
    y_positie = random.randint(-300, 300)
    kleur = random.choice(kleuren)

    teken_ster(x_positie, y_positie, kleur)

turtle.exitonclick()  # Hou het venster nog even open
