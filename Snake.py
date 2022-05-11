from asyncio.windows_events import NULL
import pygame, Global_Var as Global
import Collisions
import Game_Manager as Game_M

class Snake:    
    def __init__(self, picture):
        #Initializing snake variables
        self.picture = picture
        self.prevPic = NULL
        self.snake_X = 0
        self.snake_Y = 0
        self.snake_dx = 1
        self.snake_dy = 1

#Get functions    

    def Get_type(self):
        return type(Snake)

    def Get_snakeX(self):
        #returning the snake X
        return self.snake_X

    def Get_snakeY(self):
        #returning the snake Y
        return self.snake_Y
    
    
    def Get_picture(self):
        return self.picture

#Set functions

    def Set_snakeX(self, num):
        #updating the snake X
        self.snake_X = num
    
    def Set_snakeY(self, num):
        #updating the snake Y
        self.snake_Y = num

    def Set_picture(self, picture):
        self.picture = picture
    
    def Set_pervPic(self, picture):
        self.prevPic = picture

    
    def Draw_Cell(self, screen: pygame.Surface):
        screen.blit(self.picture,((self.Get_snakeX())*31+1,(self.Get_snakeY()*31)+66))

    
    def Change_pos(self, G: Global.Global, keypressed, GM):
        board = G.Get_Board_mat()
        X,Y = self.Get_snakeX(),self.Get_snakeY()
        if(keypressed == 3):
            Y = Y + self.snake_dy

        elif(keypressed == 4):
            X = X + self.snake_dx

        elif(keypressed == 1):
            Y = Y - self.snake_dy

        elif(keypressed == 2):
            X = X - self.snake_dx

        if(X < 0 or X > 11 or Y < 0 or Y > 13 or board[Y][X] == 1):
            GM.P_Lose()
            return False
        
        GM.Enter_snakeCell(X,Y,self.Get_picture())



    def Is_Head(self):
        return self.Head
    

    