# Theodoro Bertol Dev (Abeelha) #
# || Day 25 of #100DaysOfCode || #
import turtle
import pandas

FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("US States Game")

image = "C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 25/US_State_game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 25/US_State_game/50_states.csv")

t = turtle.Turtle()
t.hideturtle()
t.penup()


def write_state(s, x, y):
    t.goto(int(x), int(y))
    t.write(s, align="center", font=FONT)

correct_answers = []
score = 0

def check(s):
    d = data[data.state.str.lower() == s]
    global correct_answers
    if d.empty:
        print(f"Entered state {s} does not exist")
    elif d.state.item() in correct_answers:
        print(f"You already guessed {d.state.item()}")
    else:
        _extracted_from_check_9(d, correct_answers)

def _extracted_from_check_9(d, correct_answers):
    st = d.state.item()
    x = d.x
    y = d.y
    write_state(st, x, y)
    global score
    score += 1

    correct_answers.append(st)

game_is_on = True

while game_is_on:
    if score == 50:
        game_is_on = False

    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")

    if answer is None:
        game_is_on = False
        q = data.state.isin(correct_answers)
        df = data[~q]
        df.to_csv("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 25/US_State_game/missed_states.csv")
    else:
        check(answer.lower())

