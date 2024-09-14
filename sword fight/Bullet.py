import pygame

class Bullet:
    def __init__(self, x, y, vel_x, vel_y):
        self.damage = 1
        self.width = 10
        self.height = 5
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (255, 125, 125),
            (self.x, self.y, self.width, self.height),
        )

    # Devuelve el rectángulo que representa la bala
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    # Verifica colisión con un jugador
    def collide(self, player):
        return self.get_rect().colliderect(pygame.Rect(player.x, player.y, player.width, player.height))
