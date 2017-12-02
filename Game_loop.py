import pygame as pg
import json
import Player


done = False

with open("Game.conf") as json_config:
    config = json.load(json_config)
SCREEN_HEIGHT = config["SCREEN_HEIGHT"]
SCREEN_WIDTH = config["SCREEN_WIDTH"]
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FPS = config["FPS"]


pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()


def get_movement():
    pressed = pg.key.get_pressed()
    x, y = 0, 0
    if pressed[pg.K_UP]:
        y -= 1
    if pressed[pg.K_DOWN]:
        y += 1
    if pressed[pg.K_LEFT]:
        x -= 1
    if pressed[pg.K_RIGHT]:
        x += 1
    return x, y


player = Player.Player()
object1 = Player.Player(100, 100)
object2 = Player.Player(100, 200)
object3 = Player.Player(300, 100)
object4 = Player.Player(300, 200)

while not done:

    # INPUT
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    player.pos_change(*get_movement())

    # DRAW
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, BLUE, player.rect, 0)
    pg.draw.rect(screen, RED, object1.rect, 0)
    pg.draw.rect(screen, RED, object2.rect, 0)
    pg.draw.rect(screen, RED, object3.rect, 0)
    pg.draw.rect(screen, RED, object4.rect, 0)


    # UPDATE
    pg.display.flip()
    clock.tick(FPS)
