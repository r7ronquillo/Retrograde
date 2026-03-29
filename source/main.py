import pygame as pg
from player import Player

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_MIDPOINT = (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)

class Game:

    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.is_running = True
        self.player = Player(list(SCREEN_MIDPOINT))

    def start(self):
        pg.display.set_caption("Retrogate")
        self.iterate()

    def iterate(self):

        while self.is_running:
            self.get_input()
            self.screen.fill((100, 149, 237))
            self.player.draw(self.screen)
            pg.display.flip()

        self.quit()

    def get_input(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                self.is_running = False

            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    self.is_running = False

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.player.apply_thrust()

        if keys[pg.K_a]:
            self.player.turn_left()

        if keys[pg.K_d]:
            self.player.turn_right()

    def quit(self):
        pg.quit()

if __name__ == '__main__':
    game = Game()
    game.start()