import math
import pygame as pg
import json


collidables = []


class Player:
    def __init__(self, x=200, y=200, width=50, height=50):
        self.rect = pg.Rect(x, y, width, height)
        collidables.append(self.rect)
        self.speed = 2

        with open("Game.conf") as json_config:
            config = json.load(json_config)
        self.SCREEN_HEIGHT = config["SCREEN_HEIGHT"]
        self.SCREEN_WIDTH = config["SCREEN_WIDTH"]

    def pos_change(self, change_in_x, change_in_y):
        # Moves player, slower if diagonal
        if change_in_x != 0 and change_in_y != 0:
            change_in_x = change_in_x * (math.sqrt(2) / 2)
            change_in_y = change_in_y * (math.sqrt(2) / 2)

        # Collision detection
        # Compare for collisions in x direction
        new_rect_x = pg.Rect(self.rect.x + change_in_x * self.speed,
                             self.rect.y,
                             self.rect.width,
                             self.rect.height)
        for collidable in collidables:
            if collidable == self.rect:
                continue
            if new_rect_x.colliderect(collidable):
                if change_in_x > 0:
                    x_collide_point = collidable.left - self.rect.width
                if change_in_x < 0:
                    x_collide_point = collidable.right
                self.rect.x = x_collide_point
                break
        else:
            self.rect.x += change_in_x * self.speed

        # Compare for collisions in y direction
        new_rect_y = pg.Rect(self.rect.x,
                             self.rect.y + change_in_y * self.speed,
                             self.rect.width,
                             self.rect.height)
        for collidable in collidables:
            if collidable == self.rect:
                continue
            if new_rect_y.colliderect(collidable):
                if change_in_y > 0:
                    y_collide_point = collidable.top - self.rect.height
                if change_in_y < 0:
                    y_collide_point = collidable.bottom
                self.rect.y = y_collide_point
                break
        else:
            self.rect.y += change_in_y * self.speed

        self.keep_onscreen()

    def keep_onscreen(self):
        # Keeps player within display boundaries

        self.rect.right = self.SCREEN_WIDTH if self.rect.right > self.SCREEN_WIDTH else self.rect.right
        self.rect.left = 0 if self.rect.left < 0 else self.rect.left
        self.rect.bottom = self.SCREEN_HEIGHT if self.rect.bottom > self.SCREEN_HEIGHT else self.rect.bottom
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
