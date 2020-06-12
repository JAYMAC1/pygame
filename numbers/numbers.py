from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0

for dot in range(0,10):
    actor = Actor("dot")
    actor.pos = randint(20, (WIDTH - 20)), \
    randint(20,(HEIGHT - 20))
    dots.append(actor)

def draw():
    screen.fill("black")
    number = 1

    for dot in dots:
        #print("Centre: " + str(dot.center[0]) + " " + str(dot.center[1]))
        #print("Pos: " + str(dot.pos[0]) + " " + str(dot.pos[1]))
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1