import turtle, pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
score = 0
guessed_states = []
missing_states = []
# print(states_data)

states_list = states_data.state.to_list()
# print(states_list)

for i in range(0, len(states_list)):
    answer_state = screen.textinput(title=f"{score} / {len(states_list)} States Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)

        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)

        x_cor = states_data[states_data.state == answer_state].x
        y_cor = states_data[states_data.state == answer_state].y
        coordinates = (int(x_cor), int(y_cor))
        print(coordinates)

        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(coordinates)
        tim.write(answer_state, align="center", font=("Courier", 8, "normal"))

        score += 1

    else:
        print("Wrong Answer...")
