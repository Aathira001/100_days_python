import turtle
import pandas as pd

states_data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = states_data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"Guessed {len(guessed_state)}/50 States",
                                    prompt="What is another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [x for x in states if x not in guessed_state]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("States_to_learn.csv")
        break
    if answer_state in states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer = states_data[states_data.state == answer_state]
        t.goto(int(answer.x), int(answer.y))
        t.write(answer_state)

screen.exitonclick()
