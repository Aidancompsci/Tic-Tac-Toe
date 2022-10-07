import turtle
import board
import math

x_turtles = []
o_turtles = []

shape = "x"

def check_for_win():
    x_x_score = 0
    x_y_score = 0

    for turtle in x_turtles:
        x_x_score += turtle.xcor()
        x_y_score += turtle.ycor()

    if len(x_turtles) >= 3:
        if (x_x_score == 0 and   (abs(x_y_score / 150) == 1 or abs(x_y_score / 150) == 0) ) or x_y_score == 0:
            print("x  victory")
            return


def handle_game(turtles_list):
    def on_click(x, y):
        global shape

        print("on click")
        print(x, y)
        correct_turtle = None

        for turtle in turtles_list:
            if x >= turtle.xcor() - 50 and x <= turtle.xcor() + 50:
                if y >= turtle.ycor() - 50 and y <= turtle.ycor() + 50:
                    correct_turtle = turtle
                    break

        correct_turtle.hideturtle()
        if shape == "x":
            board.draw_x(correct_turtle.xcor(), correct_turtle.ycor())
            x_turtles.append(correct_turtle)
            shape = "o"
        else:
            board.draw_o(correct_turtle.xcor(), correct_turtle.ycor())
            o_turtles.append(correct_turtle)
            shape = "x"

        check_for_win()
        pass

    for turtle in turtles_list:
        turtle.onclick(on_click)



def main():
    screen = turtle.Screen()
    turtles_list = board.create_board()
    handle_game(turtles_list)

    screen.mainloop()
    pass

if __name__ == "__main__":
    main()