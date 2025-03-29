import sys

import pygame

from code.Const import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from code.GameState import GameState
from code.Menu import Menu
from code.Utils import Utils


class HighScore(GameState):
    def __init__(self, game):
        self.top_scores = []
        self.get_scores_into_database(game)

    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"[{Utils.get_formatted_date()}] [INFO] Game finished!!")
                print(f"[{Utils.get_formatted_date()}] [INFO] Closing database connection")
                game.db_proxy.close()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:  # Pressionou M para voltar ao menu
                print(f"[{Utils.get_formatted_date()}] [INFO] Return to Menu")
                pygame.time.delay(200)  # Small delay to avoid rapid state change
                game.set_state(Menu())
            else:
                pass

    def update(self, game):
        pass

    def draw(self, game):
        # Draw the screen with the top 5 scores in the game
        game.screen.fill(BLACK)
        font = pygame.font.SysFont(None, 55)
        title_text = font.render("HIGH SCORES", True, WHITE)
        game.screen.blit(title_text, (SCREEN_WIDTH // 4, 50))

        font = pygame.font.SysFont(None, 55)
        font_small = pygame.font.SysFont(None, 30)

        if len(self.top_scores) == 0:
            first_text = font.render("There are no scores saved.", True, WHITE)
            middle_text = font.render("Start the first game to see", True, WHITE)
            last_text = font.render("the top 5 scores!!", True, WHITE)
            game.screen.blit(first_text, (SCREEN_WIDTH // 9, 220))
            game.screen.blit(middle_text, (SCREEN_WIDTH // 8, 270))
            game.screen.blit(last_text, (SCREEN_WIDTH // 4, 320))
        else:
            y_offset = 200  # Initial screen position for scores
            for i in range(len(self.top_scores)):
                score = self.top_scores[i][1]
                date = self.top_scores[i][2]

                score_text = font_small.render(f"Score: {score}  Date: {date}", True, WHITE)
                game.screen.blit(score_text, (SCREEN_WIDTH // 4, y_offset))
                y_offset += 40

        # Instruction to return to the menu
        back_text = font_small.render("Press M to return the Menu!!!", True, WHITE)
        game.screen.blit(back_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT - 50))

        pygame.display.flip()

    # Get the top 5 scores in the game
    def get_scores_into_database(self, game):
        print(f"[{Utils.get_formatted_date()}] [INFO] Returning top 5 scores from the database")
        self.top_scores = game.db_proxy.get_top_scores()
