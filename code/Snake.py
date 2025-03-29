import pygame

from code.Const import CELL_SIZE, GREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from code.Utils import Utils


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # It starts with 3 parts
        self.direction = (CELL_SIZE, 0)  # Initial direction is to the right
        self.growing = False  # The snake does not grow at first
        self.score = 0  # Initial score

        self.collision_sound = pygame.mixer.Sound('./asset/knifesharpener2.flac')
        self.collision_sound.set_volume(0.2)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body = [new_head] + self.body[:-1]

        if self.growing:
            self.body.append(self.body[-1])  # The snake grows
            self.growing = False

    def grow(self, special):
        self.growing = True
        if special:
            print(f"[{Utils.get_formatted_date()}] [INFO] Ate the special food")
            self.score += 50
            collision_sound = pygame.mixer.Sound('./asset/win-176035.mp3')
            collision_sound.set_volume(0.5)
            collision_sound.play()
        else:
            print(f"[{Utils.get_formatted_date()}] [INFO] Ate the normal food")
            self.score += 10
            collision_sound = pygame.mixer.Sound('./asset/apple_bite.ogg')
            collision_sound.set_volume(0.3)
            collision_sound.play()

    def check_collision(self):
        head = self.body[0]
        # Collision with the wall
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            print(f"[{Utils.get_formatted_date()}] [INFO] Wall collision")
            self.collision_sound.play()
            return True
        # Collision with itself
        if head in self.body[1:]:
            print(f"[{Utils.get_formatted_date()}] [INFO] Collision with itself")
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
