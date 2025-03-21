import pygame

from code.Const import BLACK, CELL_SIZE
from code.DBProxy import DBProxy
from code.Snake import Snake
from code.Utils import Utils


class PlayingState:
    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        if game.snake.check_collision():
            # Salvar a pontuação no banco de dados
            db_proxy = DBProxy(db_name="snake_game_DB")
            db_proxy.save({'score': game.snake.score, 'date': Utils.get_formatted_date()})
            pygame.time.delay(500)

            from code.GameOverState import GameOverState
            game.set_state(GameOverState(game))
            pygame.mixer.music.load('./asset/game_over.mp3')
            pygame.mixer.music.play()  # Toca o som a perder o jogo
            pygame.mixer.music.play(-1)  # Fica tocando a música infinitamente
            pygame.mixer.music.set_volume(0.4)
            game.snake = Snake()

        if game.snake.body[0] == game.food.position:
            game.snake.grow()
            game.food.randomize_position()

    def draw(self, game):
        game.screen.fill(BLACK)
        game.snake.draw(game.screen)
        game.food.draw(game.screen)
        pygame.display.flip()
