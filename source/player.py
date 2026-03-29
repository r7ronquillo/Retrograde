import pygame as pg

class Player:

    def __init__(self, scale=0.5):
        self.spaceship = pg.image.load("../assets/spaceship.png").convert_alpha()

        self.spaceship = pg.transform.scale(self.spaceship, 
                                            (self.spaceship.get_width() * scale, 
                                             self.spaceship.get_height() * scale))

        self.spaceship_width = self.spaceship.get_width()
        self.spaceship_height = self.spaceship.get_height()

        self.spaceship_width_half = self.spaceship_width * 0.5
        self.spaceship_height_half = self.spaceship_height * 0.5

    def draw(self, surface: pg.surface, position: tuple):
        surface.blit(self.spaceship, 
                     (position[0] - self.spaceship_width_half, 
                      position[1] - self.spaceship_height_half))