from collections import namedtuple
import enum
import pygame, Score, Snake,Global_Var as Global, Apple

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)


Direction = [UP,DOWN, LEFT, RIGHT] 

Ai_point = namedtuple('point', 'x, y')

class Game_Manager:

    def __init__(self):
        self.screen = None
        self.Run = True
        self.clock = pygame.time.Clock()
        self.FPS = 300
        self.WIDTH = 310
        self.HEIGHT = 376
        self.Lose = False
        self.Win = False 
        self.Losing_text = "Game Over"
        self.Board = pygame.image.load("Snake_ai Pic\Board.png")
        self.snake_pic = "Snake_ai Pic\SnakeBodyRight.png"
        self.game_icon = "Snake_ai Pic\SnakeIcon.png"
        self.title = 'Snake AI'
        self.Apple = None
        self.GameScore = Score.Score()
        self.GameScore.__init__()
        self.G = Global.Global()
        self.G.__init__()
        self.StartX = 3
        self.StartY = 6
        self.LastKeypressed = 3
        self.frame_iteration = 0
        self.move_count = 0
        self.Ai = None

    
    def CreateWIN(self):
        #Creating the game borders
        pygame_icon = pygame.image.load(self.game_icon)
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(pygame_icon)

    def Check_events(self):
        #Cheking the events the player is initiating
        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        self.Run = False
        Ai_move = self.Ai.get_move(self.G.Get_Board_mat(), self.G.Get_head(), self.LastKeypressed)
        self.move_count += 1
        Head = self.G.Get_head()
        Head.Change_pos(self.G,Ai_move, self)

        if(not self.Apple.Apple_Exist(self.G)):
            self.GameScore.Update_Score()
            self.Check_win()
            self.move_count = 0
            Board = self.G.Get_Board_mat()
            print(self.Apple.Get_pos())
            self.G.Update_SnakeLength()
            if(self.Check_win()):
                return
            self.Apple.Get_apple(self.G)
        else:
            self.G.Remove_tail()


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
        self.Apple.Draw_Apple(self.screen)
        #self.Update_Snake_pos()
        self.Draw_Snake()
        self.GameScore.Draw_score(self.screen)

    def Check_win(self):
        #Cheking if the Snake legnth equal to the Board size
        if self.G.Get_SnakeLength == self.G.COLUMNS*self.G.ROWS:
            self.Win = True
            self.Run = False
            return True
        return False

    def P_Lose(self):
        #Printing massage to the player when he loses
        self.Lose = True
        #font = pygame.font.Font('freesansbold.ttf', 32)
        #text = font.render(self.Losing_text, True, (255,255,255))
        #textRect = text.get_rect()
        #self.screen.blit(text,textRect)
    
    def Create_Snake(self):
        cell = Snake.Snake(pygame.image.load(self.snake_pic))
        cell1 = Snake.Snake(pygame.image.load(self.snake_pic))
        cell.Set_snakeX(self.StartX)
        cell.Set_snakeY(self.StartY)
        cell1.Set_snakeX(self.StartX + 1)
        cell1.Set_snakeY(self.StartY)
        self.G.Insert_Head(cell)
        self.G.Insert_Head(cell1)

    def Frame_lived(self):
        return self.frame_iteration

    def Snake_Game(self, move_lim, AI, Apples):
        self.Apple = Apples
        self.Ai = AI
        #self.CreateWIN()
        self.Create_Snake()
        self.Apple.Get_apple(self.G)
        while(self.Run):
            if(move_lim > self.move_count):      
                if(self.Lose == False):
                    #self.screen.fill((0,0,0))
                    self.clock.tick(self.FPS)
                    self.frame_iteration += 1
                    self.Check_events()
                    #self.Draw_Game()
                else:
                    break
                #pygame.display.update()
            else:
                break
        #pygame.quit()
        #print(self.G.Get_head().Get_snakeY(), " , ", self.G.Get_head().Get_snakeX())
        if(self.Win):
            return -10
        return move_lim-self.move_count
