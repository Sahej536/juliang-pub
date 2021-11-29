from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will"
                            " win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
msg = Turtle()


# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


def reset(x, y):
    global is_race_on
    msg.clear()
    user_bet = screen.textinput(title="Make your bet", prompt="Which "
                                "turtle will win the race? Enter a color: ")
    for turtle_index in range(0, 6):
        all_turtles[turtle_index].penup()
        all_turtles[turtle_index].color(colors[turtle_index])
        all_turtles[turtle_index].goto(x=-230, y=y_positions[turtle_index])

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            # 230 is 250 - half the width of the turtle.
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    msg.write(f"You've won! The {winning_color}"
                              " turtle is the winner!", False, "center",
                              font=("Times", 18, "bold"))
                else:
                    msg.write(f"You've lost! The {winning_color}"
                              " turtle is the winner", False, "center",
                              font=("Times", 18, "bold"))
            # Make each turtle move a random amount.
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


button = Turtle()
button.shape("square")
button.shapesize(2, 4)
button.fillcolor("gray")
button.onclick(reset)

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                msg.write(f"You've won! The {winning_color}"
                          " turtle is the winner!", False, "center",
                          font=("Times", 18, "bold"))
            else:
                msg.write(f"You've lost! The {winning_color}"
                          " turtle is the winner", False, "center",
                          font=("Times", 18, "bold"))
        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.mainloop()
