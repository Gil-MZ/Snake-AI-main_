from pip import main
import Game_Manager as Game
from collections import deque

from Snake_AI import Snkae_AI

def main():
    pop_size = 100
    num_generations = 500
    num_trails = 1
    window_size = 7
    hidden_size = 15
    board_sizeX = 12
    board_sizeY = 14
    genetic_player = Snkae_AI(pop_size, num_generations, num_trails, window_size, hidden_size, board_sizeX, board_sizeY,
     mutation_chance = 0.2, mutation_size = 0.2)
    
    genetic_player.evolve_pop()


if __name__ == "__main__":
    main()
