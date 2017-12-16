import turtle

def lot_hex(base,depth):
    if base > depth:
        t.speed(2000)
        for i in range(6):
            t.forward(base)
            t.right(60)
        for i in range(6):
            t.forward(base/2)
            t.right(60)
        lot_hex(base/2,depth-1)
        t.forward(base)
        t.right(60)
        t.forward(base)
        t.right(60)
        lot_hex(base/2,depth-1)
        for i in range(6):
            t.forward(base/2)
            t.right(60)
        t.forward(base)
        t.right(60)
        t.forward(base)
        t.right(60)
        lot_hex(base/2,depth-1)
        for i in range(6):
            t.forward(base/2)
            t.right(60)
        t.forward(base)
        t.right(60)
        t.forward(base)
        t.right(60)


t = turtle.Turtle()
hex = turtle.Screen()
t.color("black")
lot_hex(100,15)
hex.exitonclick()