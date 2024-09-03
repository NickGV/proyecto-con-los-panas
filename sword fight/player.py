import pygame


class Player:
    def __init__(self, x, y):
        self.life = 3
        # self.attack = attack
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.lastKey = None
        self.proyectile = Proyectile(self.x, self.y, self.lastKey)

    def update(self, screen):
        self.move()
        self.draw(screen)
        self.hit(self.proyectile, screen)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.lastKey = "w"
            self.y -= 5
        if keys[pygame.K_s]:
            self.lastKey = "s"
            self.y += 5
        if keys[pygame.K_a]:
            self.lastKey = "a"
            self.x -= 5
        if keys[pygame.K_d]:
            self.lastKey = "d"
            self.x += 5

    def hit(self, hit, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            hit.draw(screen)
            hit.move()
            return
        if keys[pygame.K_q]:
            hit.draw(screen)
            hit.move()
            return

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (self.x, self.y, self.width, self.height),
        )


class Proyectile:
    def __init__(self, x, y, lastKey):
        self.damage = 1
        self.width = 10
        self.height = 5
        self.x = x
        self.y = y
        self.lastKey = lastKey

    def move(self):
        if self.lastKey == "w":
            self.y += 5
        if self.lastKey == "s":
            self.y -= 5
        if self.lastKey == "a":
            self.x -= 5
        if self.lastKey == "d":
            self.x += 5

    def draw(self, screen):
        print("print")
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (self.x, self.y, self.width, self.height)
        )
