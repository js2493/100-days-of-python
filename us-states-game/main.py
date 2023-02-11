import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

correct_answers = 0
answered_states = []
states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()

t = turtle.Turtle()
t.hideturtle()
t.penup()

while correct_answers < 50:
    answer = ""
    if correct_answers == 0:
        answer = screen.textinput(title=f"50 states left",
                                  prompt="Guess the name of a state:")
    else:
        answer = screen.textinput(title=f"{50 - correct_answers} states left",
                                  prompt="Guess the name of another state:")
    answer = answer[0:1].upper() + answer[1:].lower()
    if answer == "Exit":
        # states to learn
        missing_states = [state for state in states_data.state if state not in answered_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv").
        break
    if answer in states and answer not in answered_states:
        answered_states.append(answer)
        state_data = states_data[states_data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        correct_answers += 1





