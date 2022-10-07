import turtle
import board

turtle_spots_taken = []

shape = "x"

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
        turtle_spots_taken.append(correct_turtle)
        if shape == "x":
            board.draw_x(correct_turtle.xcor(), correct_turtle.ycor())
            shape = "o"
        else:
            board.draw_o(correct_turtle.xcor(), correct_turtle.ycor())
            shape = "x"

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