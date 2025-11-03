import turtle, pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
print(states_data)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)


screen.exitonclick()