import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.state = Menu(self)

    def handle_events(self):
        self.state.handle_input(self)

    def update(self):
        self.state.update(self)

    def draw(self):
        self.state.draw(self)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
