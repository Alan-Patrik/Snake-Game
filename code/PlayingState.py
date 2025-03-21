import pygame

from code.Const import BLACK, CELL_SIZE


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

    def draw(self, game):
        game.screen.fill(BLACK)
        game.snake.draw(game.screen)
        pygame.display.flip()
