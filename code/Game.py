import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from code.Food import Food
from code.GameOver import GameOver
from code.GameState import GameState
from code.HighScore import HighScore
from code.Menu import Menu
from code.Snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.state = Menu(self)
        self.gameOver = GameOver(self)
        self.highScore = HighScore(self)

    def set_state(self, new_state: GameState):
        self.state = new_state

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
            self.clock.tick(FPS)
