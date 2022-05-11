from pip import main
import Game_Manager as Game
from collections import deque

def main():
    #print(pygame.font.get_fonts())
    GM = Game.Game_Manager()
    GM.__init__()
    GM.Snake_Game()


if __name__ == "__main__":
    main()
