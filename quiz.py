import pgzrun

# Game Settings
TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

# Define Rectangles for Game Components
marquee_box = Rect(0, 0, 880, 80)
question_box = Rect(0, 0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

# Game State Variables
question_file_name = "Lesson14_Quiz_Master/questions.txt"
marquee_message = ""
is_game_over = False
score = 0
time_left = 10
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0
question_index = 0

# Set Positions for Boxes
marquee_box.move_ip(0, 0)
question_box.move_ip(20, 100)
timer_box.move_ip(700, 100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
skip_box.move_ip(700, 270)

# Draw the Game Screen
def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, "navy blue")
    screen.draw.filled_rect(skip_box, "dark green")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "dark orange")

    marquee_message = f"Welcome To Quiz Master... Score: {score}"
    marquee_message += f" | Q: {question_index} of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color="white")
    screen.draw.textbox(str(time_left), timer_box, color="white")
    screen.draw.textbox("Skip", skip_box, color="black", angle=-90)

    if questions:
        screen.draw.textbox(
            questions[0][0].strip(), question_box,
            color="white", shadow=(0.5, 0.5), scolor="dim grey"
        )
        index = 1
        for answer_box in answer_boxes:
            screen.draw.textbox(questions[0][index].strip(), answer_box, color="black")
            index += 1

# Load Questions
def read_question_file():
    global question_count, questions
    with open(question_file_name, "r") as q_file:
        for question in q_file:
            questions.append(question.strip().split(","))
            question_count += 1

# Time Countdown
def update_time_left():
    global time_left
    if time_left > 0:
        time_left -= 1
    else:
        game_over()

# Check Answer on Click
def on_mouse_down(pos):
    global score, questions, time_left
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == int(questions[0][5].strip()):  # Correct answer
                score += 1
                next_question()
            else:
                game_over()
        index += 1

    if skip_box.collidepoint(pos):
        next_question()

# Load Next Question
def next_question():
    global time_left
    if questions:
        questions.pop(0)
        time_left = 10
    else:
        game_over()

# End Game
def game_over():
    global marquee_message, is_game_over
    marquee_message = f"Game Over! You scored {score} points."
    is_game_over = True

# Start Game
read_question_file()
clock.schedule_interval(update_time_left, 1)

pgzrun.go()