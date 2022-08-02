from collections import deque as queue
from Apple import Apple
import Game_Manager as Game_M
import numpy, random, math


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

        self.ap = Apple()
        self.ap.Apples_Place()
        self.game = None
        self.gen = None

        self.pop = [self.generate_brain(self.window_size**2, self.hidden_size, len(Game_M.Direction)) for _ in range(self.pop_size)]

    def generate_brain(self,input_size, hidden_size, output_size):
        hidden_layer1 = numpy.array([[random.uniform(-1,1) for _ in range(input_size+1)] for _ in range(hidden_size)])
        hidden_layer2 = numpy.array([[random.uniform(-1,1) for _ in range(hidden_size+1)] for _ in range(hidden_size)])
        output_layer = numpy.array([[random.uniform(-1,1) for _ in range(hidden_size+1)] for _ in range(output_size)])

        return [hidden_layer1, hidden_layer2, output_layer]

    def get_move(self,board, snake, last_move):
        second_index = -1
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
        man_index = self.possible_moves(snake.Get_snakeX(), snake.Get_snakeY())
        second_index = self.Second_max(max_index, output_result)
        #print(max_index, " , ", second_index)
        if((max_index == 0 and last_move == 1) or (max_index == 1 and last_move == 0) or (max_index == 2 and last_move == 3) or (max_index == 3 and last_move == 2)):
            max_index = second_index
        
        if(self.gen < 50 and output_result[max_index] - output_result[second_index] > 0.3):
            max_index = man_index
        else:
            if(second_index == max_index):
                max_index = man_index
        return Game_M.Direction[max_index]
    
    def Second_max(self, max_index, output_result):
        if(max_index > 0):
            second_max_index = max_index - 1 
        else:
            second_max_index = max_index + 1
        for x in range (len(Game_M.Direction)):
            if(x != max_index):
                if(output_result[second_max_index] < output_result[x]):
                    second_max_index = x
        return second_max_index

    def manhattan_distance(self, x_head, y_head):
        #checks the distance between the snake's head coordinates and the apple's
        board = self.game.G.Get_Board_mat()
        if(x_head < 0 or x_head >= self.board_sizeX or y_head < 0 or y_head >= self.board_sizeY):
            return -1
        if(board[x_head][y_head] == 1):
            return -1
        arr_apple = self.ap.Apple_Places
        curr_apple = self.ap.current_apple
        return abs(arr_apple[curr_apple][0] - x_head) + abs(arr_apple[curr_apple][1] - y_head)
                
    def isValid(self, vis, x, y):
        board = self.game.G.Get_Board_mat()
        # If cell lies out of bounds or it's the snake's body
        if(x < 0 or x >= self.board_sizeX or y < 0 or y >= self.board_sizeY):
            return False
        if (board[x][y] == 1):
            return False
    
        # If cell is already visited
        if (vis[x][y]):
            return False
    
        # Otherwise
        return True
 
    # Function to perform the BFS traversal
    def open_spaces(self, x_head, y_head):
        possible_moves = 0
        board = self.game.G.Get_Board_mat()
        vis = [[False for _ in range(self.board_sizeX)] for _ in range (self.board_sizeY)]
        # Stores indices of the matrix cells
        q = queue()

        if(x_head < 0 or x_head >= self.board_sizeX or y_head < 0 or y_head >= self.board_sizeY):
            return -1
        if(board[x_head][y_head] == 1):
            return -1
        #Using BFS to check the number of open spaces from the snake's head coordinates
    
        # Mark the starting cell as visited
        # and push it into the queue
        q.append((x_head, y_head))
        vis[x_head][y_head] = True
    
        # Iterate while the queue
        # is not empty
        while (len(q) > 0):
            cell = q.popleft()
            x = cell[0]
            y = cell[1]    
            #q.pop()
            # Go to the adjacent cells
            adjx = x
            adjy = y
            if (self.isValid(vis, adjx+1, adjy)):
                q.append((adjx+1, adjy))
                vis[adjx+1][adjy] = True
                possible_moves += 1

            if (self.isValid(vis, adjx, adjy+1)):
                q.append((adjx, adjy+1))
                vis[adjx][adjy+1] = True
                possible_moves += 1
            
            if (self.isValid(vis, adjx-1, adjy)):
                q.append((adjx-1, adjy))
                vis[adjx-1][adjy] = True
                possible_moves += 1

            if (self.isValid(vis, adjx, adjy-1)):
                q.append((adjx, adjy-1))
                vis[adjx][adjy-1] = True
                possible_moves += 1
        return possible_moves

    def possible_moves(self, x_head, y_head):
        #Checks which path is possible and shortest
        min_x = -1
        man_dis = []
        if(self.open_spaces(x_head-1, y_head) > self.game.G.Get_SnakeLength()):#LEFT
            man_dis.append((self.manhattan_distance(x_head-1, y_head), 2))

        if(self.open_spaces(x_head+1, y_head)> self.game.G.Get_SnakeLength()):#RIGHT
            man_dis.append((self.manhattan_distance(x_head+1, y_head), 3))

        if(self.open_spaces(x_head, y_head-1)> self.game.G.Get_SnakeLength()):#UP
            man_dis.append((self.manhattan_distance(x_head, y_head-1), 0))

        if(self.open_spaces(x_head, y_head+1)> self.game.G.Get_SnakeLength()):#DOWN
            man_dis.append((self.manhattan_distance(x_head, y_head+1), 1))

        if(len(man_dis) == 0):
            man_dis.append((self.manhattan_distance(x_head-1, y_head), 2))
            man_dis.append((self.manhattan_distance(x_head+1, y_head), 3))
            man_dis.append((self.manhattan_distance(x_head, y_head-1), 0))
            man_dis.append((self.manhattan_distance(x_head, y_head+1), 1))
            max_dis = -1
            for x in range (len(man_dis)):
                dis = man_dis[x][0]
                if(dis > max_dis):
                    max_dis = man_dis[x][0]
                    min_x = man_dis[x][1]
        else:
            min_dis = 1000
            for x in range (len(man_dis)):
                dis = man_dis[x][0]
                if(dis < min_dis):
                    min_dis = man_dis[x][0]
                    min_x = man_dis[x][1]
        
        return min_x
                

    def proccess_board(self, board, x1, y1):
        #according to the board the function gives the input vector
        # x and y are the snake positions
        input_vector = [[0 for _ in range (self.window_size)] for _ in range (self.window_size)]

        for i in range(self.window_size):
            for j in range(self.window_size):
                ii = x1 + i 
                jj = y1 + j 
                #checkes if new positions are out of bounds
                if (ii < 0 or jj < 0 or ii >= self.board_sizeX or jj >= self.board_sizeY):
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
        #mutates the barin the function was given
        new_brain = []
        for layer in brain:
            new_layer = numpy.copy(layer)
            for i in range (new_layer.shape[0]):
                for j in range (new_layer.shape[1]):
                    if (random.uniform(0,1) < self.mutation_chance):
                        new_layer[i][j] +=random.uniform(-1,1)*self.mutation_size
            new_brain.append(new_layer)
        return new_brain
    
    def one_generation(self):
        #runs the current generation
        scores = [0 for _ in range(self.pop_size)]
        max_score = 0

        for i in range (self.pop_size):
            for j in range (self.num_trails):
                self.current_brain = self.pop[i]
                self.game = Game_M.Game_Manager()
                outcome = self.game.Snake_Game(300, self,self.ap)
                score = self.game.G.Get_SnakeLength()
                self.ap.reset()
                #frames = game.Frame_lived()
                #snake_length[i] += length
                if(outcome == 0):
                    score -= 2
                    print("snake ", i , " made it to last turn")
                elif(outcome == -10):
                    score+=10
                    print("snake ", i , " Won the game!")
                scores[i] += score
                if(max_score <= score):
                    max_score = score
                    print(max_score, " snake ID ", i)
                print("-------------------------------------------")
        top_25_indexes = list(numpy.argsort(scores))[3*(self.pop_size//4):self.pop_size]
        #print(snake_length, "\n")
        #print(scores, "\n\n\n")
        scores.sort(reverse=True)
        print(scores)
        top_25 = [self.pop[i] for i in top_25_indexes[::-1]]
        self.pop = self.reproduce(top_25)
        return max_score

    def evolve_pop(self):
        #The Ai loop, run on the number of generations given to him.
        max_scores = []
        for i in range (self.num_generations):
            self.gen = i
            max_scores.insert(0,self.one_generation())
            print("gen: ", i)
            print("Max Scores in every gen: ", max_scores)

        
        key = input("Enter any key to end")
        






        
