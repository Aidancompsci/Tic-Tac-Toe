import turtle

board_turtle = turtle.Turtle()
board_turtle.hideturtle()

def goto_without_pen(x, y):
    board_turtle.penup()
    board_turtle.goto(x, y)
    board_turtle.pendown()

#Each square is 50x50
def create_board():
    # left line
    goto_without_pen(-25, 75)
    board_turtle.goto(-25, -75)
    #right line
    goto_without_pen(25, 75)
    board_turtle.goto(-25, -75)
    #top line
    goto_without_pen(-75, 25)
    board_turtle.goto(75, 25)
    #bottom line
    goto_without_pen(-75, -25)
    board_turtle.goto(75, 25)


    pass
