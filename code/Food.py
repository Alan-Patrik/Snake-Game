from random import randint

import pygame

from code.Const import SCREEN_WIDTH, CELL_SIZE, SCREEN_HEIGHT, RED


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.random_food_position()
        self.color = RED

    def random_food_position(self):
        self.position = (randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))
