import pygame as pg

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Game:

    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.is_running = True

    def start(self):
        pg.display.set_caption("Retrogate")
        self.iterate()

    def iterate(self):

        while self.is_running:
            self.get_input()
            self.screen.fill((100, 149, 237))
            pg.display.flip()

        self.quit()

    def get_input(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                self.is_running = False

            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    self.is_running = False

    def quit(self):
        pg.quit()

if __name__ == '__main__':
    game = Game()
    game.start()