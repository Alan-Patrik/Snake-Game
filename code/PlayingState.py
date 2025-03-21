import pygame

from code.Const import BLACK, CELL_SIZE, WHITE
from code.GameState import GameState
from code.Snake import Snake
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
                exit()
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

        # Gerar comida especial a cada 8 segundos
        if current_time - self.last_special_spawn > 8000:
            game.special_food.spawn(current_time)
            self.last_special_spawn = current_time

            # Remover comida especial após 5 segundos
        if game.special_food.active and (current_time - game.special_food.spawn_time > 5000):
            game.special_food.active = False

        if game.snake.check_collision():
            pygame.time.delay(500)  # Aguarda até terminar de tocar a música de colisão

            print(f"[{Utils.get_formatted_date()}] [INFO] Go to the Game Over")
            pygame.mixer.music.load('./asset/game_over.mp3')
            pygame.mixer.music.play(-1)  # Toca o som a perder o jogo
            pygame.mixer.music.set_volume(0.4)

            print(f"[{Utils.get_formatted_date()}] [INFO] Saving score to database")
            # Salvar a pontuação no banco de dados
            game.db_proxy.save({'score': game.snake.score, 'date': Utils.get_formatted_date()})

            # Fazendo o import dento do metodo para evitar erro de circular import"
            from code.GameOver import GameOver
            game.set_state(GameOver(game))
            game.snake = Snake()

        if game.snake.body[0] == game.food.position:
            game.snake.grow(False)
            game.food.random_position()

        if game.snake.body[0] == game.special_food.position:
            game.snake.grow(True)
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
    font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=16)  # Fonte para exibir o tempo
    # Tempo decorrido em milissegundos
    elapsed_time = pygame.time.get_ticks() - start_time

    # Converter para minutos, segundos e milissegundos**
    minutes = (elapsed_time // 60000) % 60  # 1 minuto = 60.000ms
    seconds = (elapsed_time // 1000) % 60  # 1 segundo = 1000ms
    milliseconds = (elapsed_time % 1000) // 10  # Pegamos apenas os dois primeiros dígitos

    # Formatando a saída no formato MM:SS:mm**
    timer_text = font.render(f'Snake Game - Timeout: {minutes:02}:{seconds:02}:{milliseconds:02}', True, WHITE)
    game.screen.blit(timer_text, (20, 20))  # Desenha o timer no canto superior esquerdo


def get_current_score(game):
    font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=16)  # Fonte para exibir o tempo
    score = game.snake.score
    timer_text = font.render(f'Score: {score}', True, WHITE)
    game.screen.blit(timer_text, (20, 40))  # Desenha o timer no canto superior esquerdo
