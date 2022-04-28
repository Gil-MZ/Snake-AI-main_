from pip import main
import Game_Manager as Game
6
def main():
    #print(pygame.font.get_fonts())
    GM = Game.Game_Manager()
    GM.__init__()
    GM.Snake_Game()

if __name__ == "__main__":
    main()
