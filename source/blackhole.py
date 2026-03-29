import pygame as pg
import math
from player import Player

class Blackhole:

    def __init__(self, position=pg.Vector2(0, 0), radius=50, gravity=20):
        self.position = pg.Vector2(position)
        self.radius = radius
        self.gravity = gravity

        self.rock_position = pg.Vector2(250, 350) # FOR DEBUGGING
        self.blackhole_rotation = 0.0 # FOR DEBUGGING

    def draw(self, surface: pg.surface, player: Player):
        pg.draw.circle(surface, (0, 0, 0, 125), self.position, self.radius) # "BLACKHOLE"
        
        blachole_edge = pg.Vector2(self.rock_position.x + self.radius * math.cos(self.blackhole_rotation), 
                                   self.rock_position.y + self.radius * math.sin(self.blackhole_rotation))

        self.blackhole_rotation += 0.005 # FOR DEBUGGING
        pg.draw.circle(surface, (255, 255, 255), blachole_edge, 5) # FOR DEBUGGING ("ROCK")

        offset = self.position - player.position
        distance = offset.magnitude()

        if distance == 0:
            return

        # TESTING SPACESHIP ALIGNING WITH BLACKHOLE EDGE:
        if distance < float(self.radius * 2) and player.velocity.magnitude() < 0.8:
            player.position = blachole_edge
            print(f"Player IS in black hole orbit!") 