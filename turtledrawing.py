import turtle
turtle.speed(0)

def triangle(edge=100):
    turtle.color("blue")
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(180)

def mouse():
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.backward(50)

    turtle.pendown()
    turtle.color("blue")
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

    turtle.penup()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

    turtle.pendown()
    turtle.color("blue")
    turtle.circle(30)
    turtle.color("red")
    turtle.circle(20)

    turtle.penup()
    turtle.forward(100)

    turtle.pendown()
    turtle.color("blue")
    turtle.circle(30)
    turtle.color("red")
    turtle.circle(20)

    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)

    turtle.pendown()
    turtle.color("red")
    turtle.circle(10)

    turtle.penup()
    turtle.forward(60)

    turtle.pendown()
    turtle.circle(10)

    turtle.penup()
    turtle.backward(30)
    turtle.left(90)
    turtle.forward(20)

    turtle.pendown()
    turtle.color("black")
    turtle.left(30)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(150)

    turtle.penup()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

    turtle.pendown()
    turtle.color("red")
    turtle.circle(20,180)

triangle()
triangle()
triangle()
triangle()
triangle()
triangle()

mouse()

turtle.done()
