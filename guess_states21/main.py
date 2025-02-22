import turtle
import pandas


screen = turtle.Screen()
screen.title("India State Game")
image = r"E:\\College\\Python\\squirrel-count21\\Blank_state.gif"
screen.addshape(image)
turtle.shape(image)


guessed_states = []
while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    data = pandas.read_csv(r'E:\\College\\Python\\squirrel-count21\\28_states.csv')

    all_states = data.State.to_list()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        missing_data = pandas.DataFrame(missing_state)
        missing_data.to_csv("States_Not_Guessed.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.State == answer_state]
        t.goto(state_data.X.item(), state_data.Y.item())
        t.write(answer_state)
