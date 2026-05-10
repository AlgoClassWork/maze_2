# pip install pygame
from pygame import *

window = display.set_mode( (700, 500) )
display.set_caption('Лабиринт')

background = image.load('background.jpg')
background = transform.scale(background, (700, 500))

hero = image.load('hero.png')
hero = transform.scale(hero, (50, 50))

hero_x = 300
hero_y = 300

clock = time.Clock()

while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    window.blit( background, (0, 0) )
    window.blit( hero, (hero_x, hero_y) )

    keys = key.get_pressed()
    if keys[K_w] and hero_y > 0:
        hero_y -= 10
    if keys[K_s] and hero_y < 450:
        hero_y += 10
    if keys[K_a] and hero_x > 0:
        hero_x -= 10
    if keys[K_d] and hero_x < 650:
        hero_x += 10

    display.update()
    clock.tick(60)