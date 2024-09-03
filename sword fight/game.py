import pygame
import sys


class Game:
    def __init__(self, player1, player2):
        pygame.init()

        self.player1 = player1
        self.player2 = player2
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.fondo = pygame.image.load("./assest/fondo.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (800, 600))

    def play(self):
        pygame.display.set_caption("Pelea de espadas")
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    # elif self.player1.life <= 0 or self.player2.life <=0:
                    # running = False

            self.screen.blit(self.fondo, (0, 0))
            self.draw_players()
            self.player1.update(self.screen)
            self.player2.update(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def draw_players(self):
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
