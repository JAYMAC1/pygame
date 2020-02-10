from random import randint

apple = Actor("apple")
ball = Actor("ball")
score = 0
timer = 10

def draw():
    global score
    screen.clear()
    apple.draw()
    ball.draw()
    screen.draw.text("Score: " + str(score), topleft=(10,10))

def place_ball():
    ball.x = randint(10,800)
    ball.y = randint(10,600)

def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)

def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        score = score + 1
        print("Good shot!")
        screen.draw.text("Score: " + str(score), topleft=(10,10))
        print("Score: {0}".format(score))
        place_apple()
        place_ball()
    elif ball.collidepoint(pos):
        score = score - 2
        print("Oof, wrong item dude!!!")
        screen.draw.text("Score: "+ str(score), topleft=(10,10))
        place_ball()
        place_apple()
    else:
        print("You missed!")

place_apple()