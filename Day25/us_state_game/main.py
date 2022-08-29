import turtle
import pandas as pd
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

count_of_states = 0
data_csv = pd.read_csv("50_states.csv")
states = data_csv["state"]
know_states = []
# print(states)

while count_of_states < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{count_of_states}/50 States Correct", prompt="What's another state's name?")
    if answer_state.lower() == "exit":
        break

    for i in states:
        if answer_state.lower() == i.lower():
            count_of_states += 1
            index = states[states == answer_state.title()].index[0]
            x_cor = data_csv.loc[index, 'x']
            y_cor = data_csv.loc[index, 'y']

            State(answer_state.lower(), x_cor, y_cor)

            print(data_csv.loc[index, 'x'])
            know_states.append(index)

for i in range(len(know_states)):
    data_csv=data_csv.drop(know_states[i])

data_csv.to_csv("You_have_to_learn_these_states.csv")
