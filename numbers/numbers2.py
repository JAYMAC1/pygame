from random import randint
WIDTH = 400
HEIGHT = 400

dots = []
lines = []
max_dots = 15
next_dot = 1

for dot in range(0, max_dots):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), \
    randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), \
                        (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1

    for line in lines:
        print(line[0], line[1])
        screen.draw.line(line[0], line[1], (100, 50, 233))

def on_mouse_down(pos):
    global next_dot
    global lines

    if dot.collidepoint(pos):
        print("Ouch")

    if dots[next_dot].collidepoint(pos):
        lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1
    else:
        lines = []
        next_dot = 1