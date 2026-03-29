'''

ASSETS:
"Space Ship Construction Kit" by Skorpio (https://opengameart.org/content/space-ship-construction-kit)

'''

import pygame as pg
import math

MAX_VELOCITY = 0.9
DRAG = 0.999

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

        self.turn_amount = 0.35

        self.velocity = pg.Vector2(0, 0)
        self.thrust = 0.0025

    def draw(self, surface: pg.surface):   
        self._update_position()

        surface.blit(self.spaceship_rotated, 
                     (self.position.x - self.spaceship_width_half, 
                      self.position.y - self.spaceship_height_half))
        
    def _update_position(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        self.velocity.x *= DRAG
        self.velocity.y *= DRAG

    def apply_thrust(self):
        angle = self.rotation + 90
        self.velocity.x += math.cos(math.radians(angle)) * self.thrust
        self.velocity.y += -math.sin(math.radians(angle)) * self.thrust

        if self.velocity.magnitude() > MAX_VELOCITY:
            velocity_limit = MAX_VELOCITY / self.velocity.magnitude()
            self.velocity.x *= velocity_limit
            self.velocity.y *= velocity_limit

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