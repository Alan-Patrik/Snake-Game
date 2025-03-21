import pygame

from code.Const import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from code.DBProxy import DBProxy
from code.PlayingState import PlayingState


class Menu:
    def __init__(self, game):
        pygame.mixer.init()
        pygame.mixer.music.load('./asset/canary.ogg')
        pygame.mixer.music.play()  # Toca o som inicial do jogo
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    def handle_input(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Iniciar o jogo pressionando P
                    pygame.time.delay(200)
                    game.set_state(PlayingState())
                if event.key == pygame.K_q:  # Sair do jogo pressionando Q
                    pygame.quit()
                    db_proxy = DBProxy(db_name="snake_game_DB")
                    db_proxy.close()
                    exit()
                if event.key == pygame.K_s:  # Ver a pontuação
                    # Fazendo o import dento do metodo para evitar erro de circular import"
                    from code.HighScores import HighScores
                    pygame.time.delay(200)
                    game.set_state(HighScores(game))
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
