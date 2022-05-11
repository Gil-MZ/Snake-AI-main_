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
        self.frame_iteration = 0
    
    def reset(self):
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
        self.Lose = False
        self.Run = True
        self.frame_iteration = 0


    
    def CreateWIN(self):
        #Creating the game borders
        pygame_icon = pygame.image.load(self.game_icon)
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption('Snake AI')
        pygame.display.set_icon(pygame_icon)

    def Check_events(self):
        #Cheking the events the player is initiating
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Run = False
            elif(event.type == pygame.KEYDOWN):
                #Cheking if the player pressed W,A,S or D
                if event.key == pygame.K_w and self.LastKeypressed != 3:
                    self.Set_LastkeyPressed(1)
                elif event.key == pygame.K_a and self.LastKeypressed != 4:
                    self.Set_LastkeyPressed(2)
                elif event.key == pygame.K_s and self.LastKeypressed != 1:
                    self.Set_LastkeyPressed(3)
                elif event.key == pygame.K_d and self.LastKeypressed != 2:
                    self.Set_LastkeyPressed(4)
                elif(event.key == pygame.K_ESCAPE):
                    self.Run = False
        
        Head = self.G.Get_head()
        Head.Change_pos(self.G,self.LastKeypressed, self)


    def Enter_snakeCell(self,x,y,picture):
        New_head = Snake.Snake(picture)
        New_head.Set_snakeX(x)
        New_head.Set_snakeY(y)
        self.G.Insert_Head(New_head)
        

    def Set_LastkeyPressed(self, key):
        self.LastKeypressed = key

    def Draw_Snake(self):
        #Going through the board and printing the snake to the screen
        S_list = self.G.Get_snakeCells()
        for Cell in S_list:
            Cell.Draw_Cell(self.screen)           


    def Draw_Game(self):
        self.screen.blit(self.Board,(0,66))
        if(not self.Apple.Apple_Exist(self.G)):
            self.GameScore.Update_Score()
            if(self.Check_win()):
                return
            self.Apple.Random_place(self.screen, self.G)
        else:
            self.G.Remove_tail()
            self.Apple.Draw_Apple(self.screen)
        #self.Update_Snake_pos()
        self.Draw_Snake()
        print(len(self.G.Get_snakeCells()))
        self.GameScore.Draw_score(self.screen)

    def Check_win(self):
        #Cheking if the Snake legnth equal to the Board size
        if self.G.Get_SnakeLength == self.G.COLUMNS*self.G.ROWS:
            self.Run = False
            return True
        return False

    def P_Lose(self):
        #Printing massage to the player when he loses
        self.Lose = True
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.Losing_text, True, (255,255,255))
        textRect = text.get_rect()
        self.screen.blit(text,textRect)
    
    def Create_Snake(self):
        cell = Snake.Snake(pygame.image.load(self.snake_pic))
        cell1 = Snake.Snake(pygame.image.load(self.snake_pic))
        cell.Set_snakeX(self.StartX)
        cell.Set_snakeY(self.StartY)
        cell1.Set_snakeX(self.StartX + 1)
        cell1.Set_snakeY(self.StartY)
        self.G.Insert_Head(cell)
        self.G.Insert_Head(cell1)


    def Snake_Game(self):
        self.CreateWIN()
        print(len(self.G.Get_snakeCells()))
        self.Create_Snake()
        while(self.Run):          
            if(self.Lose == False):
                self.screen.fill((0,0,0))
                self.clock.tick(self.FPS)
                self.Check_events()
                self.Draw_Game()
                self.Check_win()
            else:
                self.P_Lose()
                self.Check_events()
            pygame.display.update()
        print(len(self.G.Get_snakeCells()))
        pygame.quit()
