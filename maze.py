# pip install pygame
from pygame import *

class GameSprite():
    def __init__(self, img, x, y):
        self.image = transform.scale(image.load(img), (50, 50))
        self.x = x 
        self.y = y

    def show(self):
        window.blit( self.image, (self.x, self.y) )

window = display.set_mode( (700, 500) )
display.set_caption('Лабиринт')

background = image.load('background.jpg')
background = transform.scale(background, (700, 500))

hero = GameSprite('hero.png', 200, 200)
enemy = GameSprite('cyborg.png', 400, 200)

clock = time.Clock()

while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    window.blit( background, (0, 0) )
    hero.show()
    enemy.show()

    keys = key.get_pressed()
    if keys[K_w] and hero.y > 0:
        hero.y -= 10
    if keys[K_s] and hero.y < 450:
        hero.y += 10
    if keys[K_a] and hero.x > 0:
        hero.x -= 10
    if keys[K_d] and hero.x < 650:
        hero.x += 10

    display.update()
    clock.tick(60)
