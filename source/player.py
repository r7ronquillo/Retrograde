'''

ASSETS:
"Space Ship Construction Kit" by Skorpio (https://opengameart.org/content/space-ship-construction-kit)

'''

import pygame as pg
import math

class Player:

    def __init__(self, init_position=pg.Vector2(0,0), init_rotation=0.0, init_scale=0.5):
        self.spaceship = pg.image.load("../assets/spaceship.png").convert_alpha()
        self.spaceship = pg.transform.scale(self.spaceship, 
                                            (self.spaceship.get_width() * init_scale, 
                                             self.spaceship.get_height() * init_scale))
        
        self.spaceship_rotated = self.spaceship
        self._update_dimensions()

        self.position = pg.Vector2(init_position)
        self.rotation = init_rotation

        self.speed = 0.5
        self.turn_amount = 0.35

    def draw(self, surface: pg.surface):
        surface.blit(self.spaceship_rotated, 
                     (self.position.x - self.spaceship_width_half, 
                      self.position.y - self.spaceship_height_half))
        
    def move_forward(self):
        self._move(self.speed)

    def move_backwards(self):
        self._move(-self.speed)

    def _move(self, move_amount):
        self.position.x += math.cos(math.radians(self.rotation + 90)) * move_amount
        self.position.y += -math.sin(math.radians(self.rotation + 90)) * move_amount

    def turn_left(self):
        self._turn(self.turn_amount)

    def turn_right(self):
        self._turn(-self.turn_amount)

    def _turn(self, turn_amount):
        self.rotation += turn_amount
        self.spaceship_rotated = pg.transform.rotate(self.spaceship, self.rotation)
        self._update_dimensions()

    def _update_dimensions(self):
        self.spaceship_width = self.spaceship_rotated.get_width()
        self.spaceship_height = self.spaceship_rotated.get_height()

        self.spaceship_width_half = self.spaceship_width * 0.5
        self.spaceship_height_half = self.spaceship_height * 0.5