import pygame

from code.Const import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from code.DBProxy import DBProxy
from code.Menu import Menu


class HighScores:
    def __init__(self, game):
        self.top_scores = []
        self.get_scores_into_database()

    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                db_proxy = DBProxy(db_name="snake_game_DB")
                db_proxy.close()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:  # Pressionou M para voltar ao menu
                pygame.time.delay(200)  # Pequeno atraso para evitar mudança rápida de estado
                game.set_state(Menu(game))
            else:
                pass

    def update(self, game):
        pass

    def draw(self, game):
        # Desenha a tela com as 5 melhores pontiuação no jogo
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
            y_offset = 200  # Posição inicial da tela para os scores
            for i in range(len(self.top_scores)):
                score = self.top_scores[i][1]
                date = self.top_scores[i][2]

                score_text = font_small.render(f"Score: {score}  Date: {date}", True, WHITE)
                game.screen.blit(score_text, (SCREEN_WIDTH // 4, y_offset))
                y_offset += 40

        # Instrução para voltar ao menu
        back_text = font_small.render("Press M to return the Menu!!!", True, WHITE)
        game.screen.blit(back_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT - 50))

        pygame.display.flip()

    # Buscar as 5 melhores pontiuação no jogo
    def get_scores_into_database(self):
        db_proxy = DBProxy("snake_game_DB")
        self.top_scores = db_proxy.get_top_scores()
