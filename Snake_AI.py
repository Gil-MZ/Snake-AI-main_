from collections import deque as queue
from Apple import Apple
import Game_Manager as Game_M
import numpy, random, math
 
# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]
 
# Function to check if a cell
# is be visited or not
def isValid(vis, row, col):
   
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= 4 or col >= 4):
        return False
 
    # If cell is already visited
    if (vis[row][col]):
        return False
 
    # Otherwise
    return True
 
# Function to perform the BFS traversal
def BFS(grid, vis, row, col):
   
    # Stores indices of the matrix cells
    q = queue()
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col ))
    vis[row][col] = True
 
    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end = " ")
 
        #q.pop()
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
 
# Driver Code
if __name__ == '__main__':
   
    # Given input matrix
    grid= [ [ 1, 2, 3, 4 ],
           [ 5, 6, 7, 8 ],
           [ 9, 10, 11, 12 ],
           [ 13, 14, 15, 16 ] ]
 
    # Declare the visited array
    vis = [[ False for i in range(4)] for i in range(4)]
    # vis, False, sizeof vis)
 
    BFS(grid, vis, 0, 0)

class Snkae_AI:

    def __init__(self, pop_size, num_generations, num_trails, window_size, hidden_size, board_sizeX, board_sizeY, mutation_chance, mutation_size):
        self.pop_size = pop_size
        self.num_generations = num_generations
        self.num_trails = num_trails
        self.window_size = window_size
        self.hidden_size = hidden_size
        self.board_sizeX = board_sizeX
        self.board_sizeY = board_sizeY
        self.mutation_chance = mutation_chance
        self.mutation_size = mutation_size

        self.display = False

        self.current_brain = None

        self.pop = [self.generate_brain(self.window_size**2, self.hidden_size, len(Game_M.Direction)) for _ in range(self.pop_size)]

    def generate_brain(self,input_size, hidden_size, output_size):
        hidden_layer1 = numpy.array([[random.uniform(-1,1) for _ in range(input_size+1)] for _ in range(hidden_size)])
        hidden_layer2 = numpy.array([[random.uniform(-1,1) for _ in range(hidden_size+1)] for _ in range(hidden_size)])
        output_layer = numpy.array([[random.uniform(-1,1) for _ in range(hidden_size+1)] for _ in range(output_size)])

        return [hidden_layer1, hidden_layer2, output_layer]

    def get_move(self,board, snake):
        input_vector = self.proccess_board(board, snake.Get_snakeX(), snake.Get_snakeY())
        hidden_layer1 = self.current_brain[0]
        hidden_layer2 = self.current_brain[1]
        output_layer = self.current_brain[2]

#        print(input_vector)
#        print(hidden_layer1[0])
        hidden_result1 = numpy.array([math.tanh(numpy.dot(input_vector, hidden_layer1[i])) for i in range (hidden_layer1.shape[0])] + [1])
        hidden_result2 = numpy.array([math.tanh(numpy.dot(hidden_result1, hidden_layer2[i])) for i in range (hidden_layer2.shape[0])] + [1])
        output_result = numpy.array([numpy.dot(hidden_result2, output_layer[i]) for i in range (output_layer.shape[0])])

        max_index = numpy.argmax(output_result)
        return Game_M.Direction[max_index]

    def proccess_board(self, board, x1, y1):
        # x and y are the snake positions
        input_vector = [[0 for _ in range (self.window_size)] for _ in range (self.window_size)]

        for i in range(self.window_size):
            for j in range(self.window_size):
                ii = x1 + i - self.window_size//2
                jj = y1 + j - self.window_size//2
                #checkes if new positions are out of bounds
                if (ii < 0 or jj < 0 or ii >= self.board_sizeY or jj >= self.board_sizeX):
                    input_vector[i][j] = -1
                elif (board[ii][jj] == 2): # apple number
                    input_vector[i][j] = 1
                elif (board[ii][jj] == 1):# snake body number
                    input_vector[i][j] = -1
                else:
                    input_vector[i][j] = 0

        if(self.display):
            print(numpy.array(input_vector))
        input_vector = list(numpy.array(input_vector).flatten()) + [1]
        return numpy.array(input_vector)
    
    def reproduce(self, top_25):
        new_pop = []
        for brain in top_25:
            new_pop.append(brain)
        for brain in top_25:
            brain = self.mutate(brain)
            new_pop.append(brain)
        #spawn new random brains
        for _ in range (self.pop_size//2):
            new_pop.append(self.generate_brain(self.window_size**2, self.hidden_size, len(Game_M.Direction)))
        return new_pop
    
    def mutate(self, brain):
        new_brain = []
        for layer in brain:
            new_layer = numpy.copy(layer)
            for i in range (new_layer.shape[0]):
                for j in range (new_layer.shape[1]):
                    if (random.uniform(0,1) < self.mutation_chance):
                        new_layer[i][j] +=random.uniform(-1,1)*self.mutation_size
            new_brain.append(new_layer)
        return new_brain
    
    def one_generation(self, apples):
        scores = [0 for _ in range(self.pop_size)]
        snake_length = [0 for _ in range(self.pop_size)]
        max_score = 0

        for i in range (self.pop_size):
            for j in range (self.num_trails):
                self.current_brain = self.pop[i]
                game = Game_M.Game_Manager()
                outcome = game.Snake_Game(150, self,apples)
                score = game.G.Get_SnakeLength()
                apples.reset()
                #frames = game.Frame_lived()
                #score = pow(length-1,3)*(frames)
                scores[i] += score
                #snake_length[i] += length
                if(outcome == 0):
                    print("snake ", i , " made it to last turn")
                elif(outcome == -10):
                    print("snake ", i , " Won the game!")
                if(max_score < score):
                    max_score = score
                    print(max_score, " snake ID ", i)
        top_25_indexes = list(numpy.argsort(scores))[3*(self.pop_size//4):self.pop_size]
        #print(snake_length, "\n")
        #print(scores, "\n\n\n")
        scores.sort(reverse=True)
        print(scores)
        top_25 = [self.pop[i] for i in top_25_indexes[::-1]]
        self.pop = self.reproduce(top_25)

    def evolve_pop(self):
        Ap = Apple()
        Ap.Apples_Places()
        for i in range (self.num_generations):
            self.one_generation(Ap)
            print("gen: ", i)
        
        key = input("Enter any key to end")
        






        