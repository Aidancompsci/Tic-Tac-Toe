import turtle

board_turtle = turtle.Turtle()
board_turtle.hideturtle()

def goto_without_pen(x, y):
    board_turtle.penup()
    board_turtle.goto(x, y)
    board_turtle.pendown()

#Each square is 100100
def create_board():
    # left line
    goto_without_pen(-50, 150)
    board_turtle.goto(-50, -150)
    #right line
    goto_without_pen(50, 150)
    board_turtle.goto(50, -150)
    #top line
    goto_without_pen(-150, 50)
    board_turtle.goto(150, 50)
    #bottom line
    goto_without_pen(-150, -50)
    board_turtle.goto(150, -50)


    squares_list = []

    for i in range(3):
        for i in range(3):
            new_turtle = turtle.Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")

    pass
