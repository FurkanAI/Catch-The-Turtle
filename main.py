import turtle
from random import randint


# For Turtle
bird = turtle.Turtle()

# score_turtle for write score on the board
score_turtle = turtle.Turtle()

# timer_turtle for write timer on the board
timer_turtle = turtle.Turtle()


game_screen_bgcolor = "light blue"  # the background color
game_time = 20  # the duration of game
game_difficulty = 5  # 1 is the easiest, 9 is the most difficult


game_over = False
score = 0


def setup_timer():
    timer_turtle.penup()
    timer_turtle.hideturtle()
    timer_turtle.color("black")
    timer_turtle.setpos(0, (turtle.window_height() / 2) - 60)


def setup_game():
    game_screen = turtle.Screen()
    game_screen.bgcolor(game_screen_bgcolor)
    game_screen.title("Catch the Turtle")


def setup_scoreboard():
    score_turtle.penup()
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.setpos(0, (turtle.window_height()/2)-30)
    score_turtle.write("Score: 0", False, "center", ("", 22, ""))


def setup_turtle():

    def click_turtle(x, y):
        global score
        score += 1
        print(f"cordinats x: {x} , y: {y}")
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", False, "center", ("", 22, ""))

    bird.penup()
    bird.hideturtle()
    bird.color("dark green")
    bird.shape("turtle")
    bird.shapesize(2, 2)
    bird.onclick(click_turtle, 1, False)


def change_position_turtle():

    if not game_over:
        bird.hideturtle()
        turtle.tracer(0)
        x_position = randint(int(-(turtle.window_width()/2-30)), int(turtle.window_width()/2-30))
        y_position = randint(int(-(turtle.window_height() / 2 - 30)), int(turtle.window_height() / 2 - 30))
        bird.setpos(x_position, y_position)
        turtle.tracer(1)
        bird.showturtle()
        turtle.ontimer(change_position_turtle, (10 - game_difficulty)*100)

    else:
        bird.hideturtle()


def countdown(time):
    global game_over
    timer_turtle.clear()
    timer_turtle.write(f"Time Left: {time}", False, "center", ("", 22, ""))

    if time > 0:
        turtle.ontimer(lambda: countdown(time-1), 1000)
    else:
        game_over = True
        setup_game_over()


def setup_game_over():

    timer_turtle.clear()
    timer_turtle.home()
    timer_turtle.write("Game Over", False, "center", ("", 22, ""))


def start_up():
    global game_time
    turtle.tracer(0)
    setup_game()
    setup_turtle()
    setup_scoreboard()
    setup_timer()
    countdown(game_time)
    change_position_turtle()
    turtle.tracer(1)


start_up()

turtle.mainloop()
