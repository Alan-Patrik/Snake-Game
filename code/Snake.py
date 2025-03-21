import pygame

from code.Const import CELL_SIZE, GREEN


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Começa com 3 partes
        self.direction = (CELL_SIZE, 0)  # Direção inicial é para a direita
        self.growing = False  # A cobra não cresce no início
        self.score = 0  # Pontuação inicial

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body = [new_head] + self.body[:-1]

        if self.growing:
            self.body.append(self.body[-1])  # Cresce a cobra
            self.growing = False

    def grow(self):
        self.growing = True

    def change_direction(self, new_direction):
        if self.direction[0] == -new_direction[0] and self.direction[1] == -new_direction[1]:
            return
        self.direction = new_direction

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
