import turtle
import pandas

screen = turtle.Screen()
screen.title("Штаты США")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_list = pandas.read_csv("50_states.csv")
all_states = states_list.state.to_list()
print(all_states)
state_count = []

while len(state_count) < 50:
    answer_state = screen.textinput(title=f"{len(state_count)}/50", prompt="Название штата: ").title()

    if answer_state in all_states:
        state_count.append(answer_state)
        state = states_list[states_list.state == answer_state]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)

    elif answer_state == "Exit":
        missing_states = [state for state in all_states if state not in state_count]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learning.csv")
        break
