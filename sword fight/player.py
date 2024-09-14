import pygame
from Bullet import Bullet

# Crear un diccionario de controles, que se pasan por parametro a la clase

class Player:
    def __init__(self, x, y, controls):
        self.life = 3
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.lastKey = None
        self.controls = controls
        

    # TODO: mandar la key que se presiono para moverlo
    def move(self, keys_pressed):
        if keys_pressed[self.controls["up"]]:
            self.y -= 5
            self.lastKey = "UP"
        if keys_pressed[self.controls["down"]]:
            self.y += 5
            self.lastKey = "DOWN"
        if keys_pressed[self.controls["left"]]:
            self.x -= 5
            self.lastKey = "LEFT"
        if keys_pressed[self.controls["right"]]:
            self.x += 5
            self.lastKey = "RIGHT"
            
    # Crear la bullet desde la funcion shot, para que se puedan crear varias
    def shoot(self):
        if self.lastKey == None:
            return None

        if self.lastKey == "UP":
            return Bullet(self.x + self.width // 2, self.y - self.height // 2, 0, -5)
        
        if self.lastKey == "DOWN":
            return Bullet(self.x + self.width // 2, self.y + self.height, 0, 5)
        
        if self.lastKey == "LEFT":
            return Bullet(self.x - self.width // 2, self.y + self.height // 2, -5, 0)

        if self.lastKey == "RIGHT":
            return Bullet(self.x + self.width, self.y + self.height // 2, 5, 0)


    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (255, 0, 125),
            (self.x, self.y, self.width, self.height),
        )

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
