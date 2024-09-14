from Player import Player
from Game import Game
from Bullet import Bullet
import pygame

def main():

    player1 = Player(
        30,
        30,
        {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d},
    )
    player2 = Player(
        740,
        550,
        {
            "up": pygame.K_UP,
            "down": pygame.K_DOWN,
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
        },
    )
    game = Game(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
