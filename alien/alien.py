WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
alien.pos = (400, 50)
#box = Rect((20,20),(100,100))

zombie = Actor('zombie')
zombie.pos = (200, 50)

background = Actor('background')

def draw():
    screen.clear()
    background.draw()
    alien.draw()
    #screen.draw.filled_rect(box,"red")
    zombie.draw()

def update():
    if keyboard.right or keyboard.d:
        alien.x += + 2
    elif keyboard.left or keyboard.a:
        alien.x += - 2
    elif keyboard.down or keyboard.s:
        alien.y += + 2
    elif keyboard.up or keyboard.w:
        alien.y += - 2
    if zombie.x < alien.x:
        zombie.x += + 1
    if zombie.x > alien.x:
        zombie.x += - 1
    if zombie.y < alien.y:
        zombie.y += + 1
    if zombie.y > alien.y:
        zombie.y += - 1
    #if alien.colliderect(box):
    #    exit()
