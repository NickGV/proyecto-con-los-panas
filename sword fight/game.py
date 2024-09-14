import pygame
import sys

# Dicionario de esta forma {'up', pygame_K_w, 'down', pygame_K_s, 'left', pygame_K_a, 'right', pygame_K_d}
class Game:
    def __init__(self, player1, player2):
        pygame.init()
        self.player1 = player1
        self.player2 = player2
        self.bullets = []
        self.screen = pygame.display.set_mode((800, 600))
        self.fondo = pygame.image.load("./assest/fondo.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (800, 600))

    def play(self):
        pygame.display.set_caption("Pelea de espadas")
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)
            # TODO: manejar los eventos 
            keys_pressed = pygame.key.get_pressed()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = self.player1.shoot()
                        if bullet:
                            self.bullets.append(bullet)
                    if event.key == pygame.K_q:
                        bullet = self.player2.shoot()
                        if bullet:
                            self.bullets.append(bullet)

            self.screen.blit(self.fondo, (0, 0))
            self.player1.move(keys_pressed)
            self.player2.move(keys_pressed)
            
            # TODO: Hacer que las balas se muevan
            for bullet in self.bullets:
                bullet.update()
            # TODO: Hacer que las balas colisionen con los jugadores con ambos y bajarles una vida
            for bullet in self.bullets:
                    if bullet.collide(self.player1) or bullet.collide(self.player2):
                        self.player1.life -= 1
                        self.player2.life -= 1
                        self.bullets.remove(bullet)
                        if self.player1.life <= 0:
                            print("Player 1 ha perdido")
                            running = False
                        if self.player2.life <= 0:
                            print("Player 2 ha perdido")
                            running = False

            # TODO: Remover las balas que salgan de la pantalla
            self.bullets = [bullet for bullet in self.bullets if 0 < bullet.x < 800 and 0 < bullet.y < 600]

            self.draw()
            

    def draw(self):
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        
        # TODO: Pintar tambien las balas
        for bullet in self.bullets:
            bullet.draw(self.screen)
            
        pygame.display.flip()

    def collide(self, player):
        return (
            self.x < player.x + player.width and
            self.x + self.width > player.x and
            self.y < player.y + player.height and
            self.y + self.height > player.y
        )
        
