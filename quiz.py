import pgzrun

WIDTH = 900
HEIGHT = 700
TITLE = "QuizMaster"

markybox = Rect(450, 50, 900, 100)
questionbox = Rect(400, 150, 900, 100)
timerbox = Rect(850, 125, 100, 100)
optionbox1 = Rect(150, 263, 300, 250)
optionbox2 = Rect(150, 325, 300, 250)
optionbox3 = Rect(450, 263, 300, 250)
optionbox4 = Rect(450, 325, 300, 250)
skipbox = Rect(750, 400, 300, 400)

questionfile = "quiz master/questions.txt"

Markymessage = ""

answerboxes = [optionbox1, optionbox2, optionbox3, optionbox4]
questions = []
questioncount = 0
questionindex = 0

markybox.move_ip(0, 0)
questionbox.move_ip(20, 100)
timerbox.move_ip(700, 100)
optionbox1.move_ip(20, 220)
optionbox2.move_ip(320, 220)
optionbox3.move_ip(20, 540)
optionbox4.move_ip(320, 540)
skipbox.move_ip(170, 720)

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(markybox, "black")
    screen.draw.filled_rect(questionbox, "blue")
    screen.draw.filled_rect(timerbox, "blue")
    screen.draw.filled_rect(optionbox1, "yellow")
    screen.draw.filled_rect(optionbox2, "yellow")
    screen.draw.filled_rect(optionbox3, "yellow")
    screen.draw.filled_rect(optionbox4, "yellow")

pgzrun.go()