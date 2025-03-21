import pygame

from code.Const import CELL_SIZE, GREEN, SCREEN_WIDTH, SCREEN_HEIGHT


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Começa com 3 partes
        self.direction = (CELL_SIZE, 0)  # Direção inicial é para a direita
        self.growing = False  # A cobra não cresce no início
        self.score = 0  # Pontuação inicial

        self.collision_sound = pygame.mixer.Sound('./asset/knifesharpener2.flac')
        self.collision_sound.set_volume(0.2)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body = [new_head] + self.body[:-1]

        if self.growing:
            self.body.append(self.body[-1])  # Cresce a cobra
            self.growing = False

    def grow(self, special):
        self.growing = True
        if special:
            self.score += 50  # Comida especial vale 50 pontos
            collision_sound = pygame.mixer.Sound('./asset/win-176035.mp3')
            collision_sound.set_volume(0.5)
            collision_sound.play()
        else:
            self.score += 10  # Comida normal vale 10 pontos
            collision_sound = pygame.mixer.Sound('./asset/apple_bite.ogg')
            collision_sound.set_volume(0.3)
            collision_sound.play()

    def check_collision(self):
        head = self.body[0]
        # Colisão com a parede
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            self.collision_sound.play()
            return True
        # Colisão consigo mesma
        if head in self.body[1:]:
            self.collision_sound.play()
            return True
        return False

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
