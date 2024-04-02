import turtle

turtle.speed(0)

def teken_ster(x, y, kleur="yellow"):
    """
    Tekent een ster met grootte 50, op aangeduide locatie (x, y)
    in een eventueel meeggegeven kleur (default geel).
    """
    grootte = 50  # Vaste grootte van de ster
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor(kleur)
    turtle.begin_fill()

    for _ in range(5):
        turtle.forward(grootte)
        turtle.right(144)

    turtle.end_fill()