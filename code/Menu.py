import pygame

from code.Const import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from code.PlayingState import PlayingState


class Menu:
    def __init__(self, game):
        pygame.mixer.init()

    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Iniciar o jogo pressionando P
                    pygame.time.delay(200)
                    game.state = PlayingState()
            else:
                pass

    def update(self, game):
        pass

    def draw(self, game):
        game.screen.fill(BLACK)
        font = pygame.font.SysFont(None, 55)
        title = font.render("SNAKE GAME", True, WHITE)
        start_text = font.render("Press P to Play", True, WHITE)
        quit_text = font.render("Press Q to Quit", True, WHITE)
        last_score = font.render("Press S to Score", True, WHITE)

        game.screen.blit(title, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4))
        game.screen.blit(start_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        game.screen.blit(quit_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 50))
        game.screen.blit(last_score, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 100))

        pygame.display.flip()
