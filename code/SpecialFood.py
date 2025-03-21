from random import randint

import pygame

from code.Const import BLUE, SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE


class SpecialFood:
    def __init__(self):
        self.position = (0, 0)
        self.color = BLUE
        self.active = False
        self.spawn_time = 0

    def spawn(self, current_time):
        self.position = (randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        self.active = True
        self.spawn_time = current_time

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))
