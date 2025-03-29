import sys

import pygame

from code.Const import BLACK, CELL_SIZE, WHITE
from code.Food import Food
from code.GameState import GameState
from code.Snake import Snake
from code.SpecialFood import SpecialFood
from code.Utils import Utils


class PlayingState(GameState):
    def __init__(self):
        self.start_time = pygame.time.get_ticks()  # Guarda o tempo inicial do jogo
        self.last_special_spawn = pygame.time.get_ticks()

    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"[{Utils.get_formatted_date()}] [INFO] Game finished!!")
                print(f"[{Utils.get_formatted_date()}] [INFO] Closing database connection")
                game.db_proxy.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.change_direction((0, -CELL_SIZE))
                elif event.key == pygame.K_DOWN:
                    game.snake.change_direction((0, CELL_SIZE))
                elif event.key == pygame.K_LEFT:
                    game.snake.change_direction((-CELL_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    game.snake.change_direction((CELL_SIZE, 0))

    def update(self, game):
        game.snake.move()
        current_time = pygame.time.get_ticks()

        # Generate special food every 8 seconds
        if current_time - self.last_special_spawn > 8000:
            game.special_food.random_special_food_position(current_time)
            self.last_special_spawn = current_time

        # Remove special food after 5 seconds
        if game.special_food.active and (current_time - game.special_food.spawn_time > 4000):
            game.special_food.active = False

        if game.snake.check_collision():
            pygame.time.delay(500)  # Wait until the collision music finishes playing

            print(f"[{Utils.get_formatted_date()}] [INFO] Go to the Game Over")
            pygame.mixer.music.load('./asset/game_over.mp3')
            pygame.mixer.music.play(-1)  # Play the sound of losing the game
            pygame.mixer.music.set_volume(0.4)

            print(f"[{Utils.get_formatted_date()}] [INFO] Saving score to database")
            # Save the score to the database
            game.db_proxy.save({'score': game.snake.score, 'date': Utils.get_formatted_date()})

            # Doing the import inside the method to avoid circular import error
            from code.GameOver import GameOver
            game.set_state(GameOver(game))
            game.snake = Snake()
            game.food = Food()
            game.special_food = SpecialFood()

        if game.snake.body[0] == game.food.position:
            game.snake.grow(False)

            if game.food.position not in game.snake.body[0]:
                game.food.random_food_position()

        if game.snake.body[0] == game.special_food.position:
            game.snake.grow(True)
            if game.special_food.position not in game.snake.body[0]:
                game.special_food.random_special_food_position(current_time)
                game.special_food.active = False  # Desativa a comida especial após ser comida

    def draw(self, game):
        game.screen.fill(BLACK)
        game.snake.draw(game.screen)
        game.food.draw(game.screen)
        game.special_food.draw(game.screen)
        get_current_time_game(game, self.start_time)
        get_current_score(game)

        pygame.display.flip()


def get_current_time_game(game, start_time):
    try:
        font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=16)  # Fonte para exibir o tempo
        # Elapsed time in milliseconds
        elapsed_time = pygame.time.get_ticks() - start_time

        # Convert to minutes, seconds and milliseconds
        minutes = (elapsed_time // 60000) % 60  # 1 minute = 60.000ms
        seconds = (elapsed_time // 1000) % 60  # 1 second = 1000ms
        milliseconds = (elapsed_time % 1000) // 10  # We only take the first two digits

        # Formatting output in MM:SS:mm format
        timer_text = font.render(f'Snake Game - Timeout: {minutes:02}:{seconds:02}:{milliseconds:02}', True, WHITE)
        game.screen.blit(timer_text, (20, 20))  # Draw the timer in the upper left corner
    except Exception as e:
        print(f"Erro ao exibir tempo do jogo: {e}")


def get_current_score(game):
    font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=16)  # Font to display time
    score = game.snake.score
    timer_text = font.render(f'Score: {score}', True, WHITE)
    game.screen.blit(timer_text, (20, 40))  # Draw the timer in the upper left corner
