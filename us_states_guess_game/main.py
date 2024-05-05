import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('US States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv('50_states.csv')

correct_guess = 0
df['standard_state'] = df['state'].str.lower()
all_states = df['standard_state'].to_list()
correct_answer_guess_list = []

while correct_guess < 50:
    answer_state = screen.textinput(title=f"{correct_guess}/{len(all_states)} States Correct", prompt="What's another state name?").lower()
    if answer_state in all_states and answer_state not in correct_answer_guess_list:
        correct_guess += 1
        correct_answer_guess_list.append(answer_state)
        correct_answer_x = df[df['standard_state']==answer_state]['x'].values[0]
        correct_answer_y = df[df['standard_state']==answer_state]['y'].values[0]
        correct_answer = df[df['standard_state']==answer_state]['state'].values[0]
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        label.goto(correct_answer_x, correct_answer_y)
        label.write(correct_answer, align='center')
    elif answer_state == 'exit':
        break

# screen.exitonclick()