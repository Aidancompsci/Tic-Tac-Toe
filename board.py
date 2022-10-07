import turtle

board_turtle = turtle.Turtle()
board_turtle.hideturtle()
board_turtle.speed(0)

def goto_without_pen(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def on_click(x,y):
    print("clicked")

#Each square is 100100
def create_board():
    # left line
    goto_without_pen(board_turtle, -50, 150)
    board_turtle.goto(-50, -150)
    #right line
    goto_without_pen(board_turtle, 50, 150)
    board_turtle.goto(50, -150)
    #top line
    goto_without_pen(board_turtle, -150, 50)
    board_turtle.goto(150, 50)
    #bottom line
    goto_without_pen(board_turtle, -150, -50)
    board_turtle.goto(150, -50)

    squares_list = []

    for j in range(3):
        for k in range(3):
            new_turtle = turtle.Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            goto_without_pen(new_turtle, (-100 + (100 * j)), (100 + (-100 * k)))
            new_turtle.shapesize(4.9)
            squares_list.append(new_turtle)
            

    return squares_list

def draw_x(x, y):
    goto_without_pen(board_turtle, x, y)
    board_turtle.setheading(45)
    board_turtle.forward(40)
    board_turtle.backward(80)

    goto_without_pen(board_turtle, x, y)
    board_turtle.setheading(315)
    board_turtle.forward(40)
    board_turtle.backward(80)
    pass

def draw_o(x, y):
    board_turtle.setheading(0)
    goto_without_pen(board_turtle, x, (y-40))
    board_turtle.circle(40)
    pass

