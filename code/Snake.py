import pygame

from code.Const import CELL_SIZE, GREEN


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Começa com 3 partes
        self.direction = (CELL_SIZE, 0)  # Direção inicial é para a direita
        self.score = 0  # Pontuação inicial

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body = [new_head] + self.body[:-1]

    def change_direction(self, new_direction):
        if self.direction[0] == -new_direction[0] and self.direction[1] == -new_direction[1]:
            return
        self.direction = new_direction

    def move_towards_food(self, food_position):
        head_x, head_y = self.body[0]
        food_x, food_y = food_position

        if head_x < food_x:
            self.change_direction((CELL_SIZE, 0))
        elif head_x > food_x:
            self.change_direction((-CELL_SIZE, 0))
        elif head_y < food_y:
            self.change_direction((0, CELL_SIZE))
        elif head_y > food_y:
            self.change_direction((0, -CELL_SIZE))

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
