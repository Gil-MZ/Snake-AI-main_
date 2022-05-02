from asyncio.windows_events import NULL
from collections import deque
import pygame, Collisions, Score,Snake,Global_Var as Global, Apple

class Game_Manager:

    def __init__(self):
        self.screen = NULL
        self.Run = True
        self.clock = pygame.time.Clock()
        self.FPS = 5
        self.WIDTH = 373
        self.HEIGHT = 500
        self.Lose = False
        self.Losing_text = "Game Over"
        self.Board = pygame.image.load("Snake_ai Pic\Board.png")
        self.snake_pic = "Snake_ai Pic\SnakeBodyRight.png"
        self.game_icon = "Snake_ai Pic\SnakeIcon.png"
        self.Apple = Apple.Apple()
        self.Apple.__init__()
        self.GameScore = Score.Score()
        self.GameScore.__init__()
        self.G = Global.Global()
        self.G.__init__()
        self.C = Collisions.Collisions()
        self.C.__init__()
        self.StartX = 3
        self.StartY = 6
        self.LastKeypressed = 4
    
    def CreateWIN(self):
        #Creating the game borders
        pygame_icon = pygame.image.load(self.game_icon)
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption('Snake AI')
        pygame.display.set_icon(pygame_icon)

    def Check_events(self):
        #Cheking the events the player is initiating
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Run = False
            elif(event.type == pygame.KEYDOWN):
                S_queue = self.G.Get_snakeCells()
                Head = S_queue.popleft()
                #Cheking if the player pressed W,A,S or D
                if event.key == pygame.K_w and self.LastKeypressed != 3:
                    self.Set_LastkeyPressed(1)
                elif event.key == pygame.K_a and self.LastKeypressed != 4:
                    self.Set_LastkeyPressed(2)
                elif event.key == pygame.K_s and self.LastKeypressed != 1:
                    self.Set_LastkeyPressed(3)
                elif event.key == pygame.K_d and self.LastKeypressed != 2:
                    self.Set_LastkeyPressed(4)
                self.G.Set_Snake_cells_Right(Head)
                self.Update_Snake_pos()

    def Enter_snakeCell(self):
        #Adding another cell to the snake queue
        S_queue = self.G.Get_snakeCells()
        Snake_cell = NULL
        #If the head is created
        if(self.G.Get_SnakeLength() == 0):
            Snake_pic = pygame.image.load(self.snake_pic)
            Snake_cell = Snake.Snake(Snake_pic, self.G, True)
            Snake_cell.Set_snakeX(self.StartX)
            Snake_cell.Set_snakeY(self.StartY)
            self.G.Set_Board_mat(self.StartY, self.StartX, 3)
        #The rest of the body
        else:
            Cell = S_queue.pop()
            self.G.Set_Snake_cells(Cell)
            Snake_cell = Snake.Snake(Cell.Get_picture(),self.G,False)
            Snake_cell.Update_Cell(Cell, self.G)
            self.G.Set_Board_mat(Snake_cell.Get_snakeY(), Snake_cell.Get_snakeX(), 1)
        board = self.G.Get_Board_mat()
        self.G.Set_Snake_cells(Snake_cell)
        self.G.Update_SnakeLength()

    def Set_LastkeyPressed(self, key):
        self.LastKeypressed = key

    def Draw_Snake(self):
        #Going through the board and printing the snake to the screen
        S_queue = self.G.Get_snakeCells()
        temp = S_queue.copy()
        Cell = NULL
        while(temp):
            Cell = temp.popleft()
            Cell.Draw_Cell(self.screen)

                    
    
    def Update_Snake_pos(self):
        #Changes the snake position due to a WASD keys being pressed
        S_queue = self.G.Get_snakeCells()
        Cell = S_queue.popleft()
        if(Cell.Change_pos(self.LastKeypressed, self.G, self.LastKeypressed, self) == False):
            return
        self.G.Set_Snake_cells_Right(Cell)
        board = self.G.Get_Board_mat()
        Cell1 = NULL
        while(S_queue):
            Cell1 = S_queue.popleft()
            if(Cell1.Is_Head()):
                self.G.Set_Snake_cells_Right(Cell1)
                break
            Cell1.Update_Cell(Cell, self.G)
            self.G.Set_Snake_cells(Cell1)
            Cell = Cell1
        self.G.Set_Board_mat(Cell.Get_snakepervY(), Cell.Get_snakepervX(), 0)
        board = self.G.Get_Board_mat()
        S_queue = self.G.Get_snakeCells()
        print("bla")

            


    def Draw_Game(self):
        self.screen.blit(self.Board,(0,66))
        if(not self.Apple.Apple_Exist(self.G)):
            self.Enter_snakeCell()
            self.GameScore.Update_Score()
            self.Apple.Random_place(self.screen, self.G)
        else:
            self.Apple.Draw_Apple(self.screen)
        self.Update_Snake_pos()
        self.Draw_Snake()
        print(len(self.G.Get_snakeCells()))
        self.GameScore.Draw_score(self.screen)

    def Check_win(self):
        #Cheking if the Snake legnth equal to the Board size
        if self.G.Get_SnakeLength == self.G.COLUMNS*self.G.ROWS:
            self.Run = False

    def P_Lose(self):
        #Printing massage to the player when he loses
        self.Lose = True
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.Losing_text, True, (255,255,255))
        textRect = text.get_rect()
        self.screen.blit(text,textRect)

    def Snake_Game(self):
        self.CreateWIN()
        print(len(self.G.Get_snakeCells()))
        while(self.Run):
            if(self.Lose == False):
                self.screen.fill((0,0,0))
                self.clock.tick(self.FPS)
                self.Check_events()
                self.Draw_Game()
                self.Check_win()
            else:
                self.P_Lose()
            pygame.display.update()
        print(len(self.G.Get_snakeCells()))
        pygame.quit()
