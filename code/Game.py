import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from code.Food import Food
from code.GameOverState import GameOverState
from code.Menu import Menu
from code.Snake import Snake

# TENHO QUE CONTINUAR COM O STATE, TERMINAR O MENU COM AS OUTRAS OPÇÕES E TBM COLOCAR O TIMER NA TELA DO JOGO

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.state = Menu(self)
        self.gameOver = GameOverState(self)

    def set_state(self, new_state):
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
