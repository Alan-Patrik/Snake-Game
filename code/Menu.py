import sys

import pygame

from code.Const import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from code.GameState import GameState
from code.PlayingState import PlayingState
from code.Utils import Utils


class Menu(GameState):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./asset/canary.ogg')
        pygame.mixer.music.play()  # Toca o som inicial do jogo
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"[{Utils.get_formatted_date()}] [INFO] Game finished!!")
                print(f"[{Utils.get_formatted_date()}] [INFO] Closing database connection")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Start the game by pressing P
                    print(f"[{Utils.get_formatted_date()}] [INFO] Go to the Playing State")
                    pygame.time.delay(200)
                    game.set_state(PlayingState())
                if event.key == pygame.K_q:  # Quit the game by pressing Q
                    print(f"[{Utils.get_formatted_date()}] [INFO] Game finished!!")
                    print(f"[{Utils.get_formatted_date()}] [INFO] Closing database connection")
                    pygame.quit()
                    game.db_proxy.close()
                    sys.exit()
                if event.key == pygame.K_s:  # View Score
                    print(f"[{Utils.get_formatted_date()}] [INFO] Go to the High Scores")
                    pygame.time.delay(200)

                    # Doing the import inside the method to avoid circular import error
                    from code.HighScore import HighScore
                    game.set_state(HighScore(game))
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
