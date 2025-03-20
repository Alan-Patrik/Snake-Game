import pygame

from code.Const import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT


class Menu:
    def __init__(self, game):
        self.game = game

    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                pass

    def update(self, game):
        pass

    def draw(self, game):
        self.game.screen.fill(BLACK)
        font = pygame.font.SysFont(None, 55)
        title = font.render("SNAKE GAME", True, WHITE)
        start_text = font.render("Press P to Play", True, WHITE)
        quit_text = font.render("Press Q to Quit", True, WHITE)
        last_score = font.render("Press S to Score", True, WHITE)

        self.game.screen.blit(title, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4))
        self.game.screen.blit(start_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        self.game.screen.blit(quit_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 50))
        self.game.screen.blit(last_score, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 100))

        pygame.display.flip()
