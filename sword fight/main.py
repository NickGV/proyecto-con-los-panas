from player import Player
from game import Game
def main():
    player1 = Player(30,30)
    player2 = Player(740,550)
    game = Game(player1, player2)
    game.play()
    
if __name__ == "__main__":
    main()