import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from code.DBProxy import DBProxy
from code.Food import Food
from code.GameState import GameState
from code.Menu import Menu
from code.Snake import Snake
from code.SpecialFood import SpecialFood
from code.Utils import Utils


class Game:
    def __init__(self):
        try:
            print(f"[{Utils.get_formatted_date()}] [INFO] Start Game!!")
            pygame.init()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.clock = pygame.time.Clock()
            self.db_proxy = DBProxy(db_name="snake_game_DB")
            self.snake = Snake()
            self.food = Food()
            self.special_food = SpecialFood()
            self.state = Menu()
        except Exception as e:
            print(f"Error starting the game: {e}")

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
            try:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(FPS)
            except Exception as e:
                print(f"Error during game execution: {e}")
