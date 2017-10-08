import turtle

def draw_square():
    #Window for drawing
    window = turtle.Screen()
    window.bgcolor("red")

    #brad is moving
    brad = turtle.Turtle()
    turtle.shape("turtle")
    turtle.pencolor("green")
    turtle.speed(9)
    
    
    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)


    window.exitonclick()

draw_square()
