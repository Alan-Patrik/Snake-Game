import pygame

from code.Const import BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE
from code.DBProxy import DBProxy
from code.State import State


class GameOverState(State, ):
    def __init__(self, game):
        super().__init__(game)
        self.last_score = None
        self.score = 0
        self.get_score_into_database()

    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                db_proxy = DBProxy(db_name="snake_game_DB")
                db_proxy.close()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                from code.Menu import Menu
                pygame.time.delay(200)  # Pequeno atraso para evitar mudança rápida de estado
                game.set_state(Menu(game))
            else:
                pass

    def update(self, game):
        pass

    def draw(self, game):
        for i in range(len(self.last_score)):
            self.score = self.last_score[i][1]

        title = "GAME OVER"
        sub_title = f"Score: {self.score}"

        self.game.screen.fill(BLACK)
        font = pygame.font.SysFont(None, 55)
        font_small = pygame.font.SysFont(None, 30)

        text_title = font.render(title, True, WHITE)
        text_sub_title = font.render(sub_title, True, WHITE)

        self.game.screen.blit(text_title, (((SCREEN_WIDTH / 2) - (len(title) + 100)), (SCREEN_HEIGHT / 4)))
        self.game.screen.blit(text_sub_title, (((SCREEN_WIDTH / 2) - (len(sub_title) + 80)), (SCREEN_HEIGHT / 2)))

        back_text = font_small.render("Press M to return the Menu!!!", True, WHITE)
        self.game.screen.blit(back_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT - 50))

        pygame.display.flip()

    def get_score_into_database(self):
        db_proxy = DBProxy(db_name="snake_game_DB")
        self.last_score = db_proxy.get_last_score()
