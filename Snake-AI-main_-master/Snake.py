from asyncio.windows_events import NULL
import pygame, Global_Var as Global
import Collisions
import Game_Manager as Game_M

class Snake:    
    def __init__(self, picture, G: Global.Global, H: bool):
        #Initializing snake variables
        self.Head = H
        self.picture = picture
        self.prevPic = NULL
        self.snake_X = 0
        self.snake_Y = 0
        self.snake_pervX = 0
        self.snake_pervY = 0
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
    
    def Get_snakepervX(self):
        #returning the snake previouse X
        return self.snake_pervX

    def Get_snakepervY(self):
        #returning the snake previouse Y
        return self.snake_pervY
    
    def Get_picture(self):
        return self.picture

#Set functions

    def Set_snakeX(self, num):
        #updating the snake X
        self.snake_X = num
    
    def Set_snakeY(self, num):
        #updating the snake Y
        self.snake_Y = num

    def Set_snakepervX(self, num):
        #updating the snake previouse X
        self.snake_pervX = num
    
    def Set_snakepervY(self, num):
        #updating the snake previouse Y
        self.snake_pervY = num

    def Set_picture(self, picture):
        self.picture = picture
    
    def Set_pervPic(self, picture):
        self.prevPic = picture

    def Update_Cell(self, NextCell , G: Global.Global):
        #updating the snake Location to the Next snake's cell
        self.Set_snakepervX(self.Get_snakeX())
        self.Set_snakepervY(self.Get_snakeY())
        self.Set_pervPic(self.picture)
        self.Set_snakeX(NextCell.Get_snakepervX())
        self.Set_snakeY(NextCell.Get_snakepervY())
        self.Set_picture(NextCell.Get_picture())
        G.Set_Board_mat(self.Get_snakepervY(), self.Get_snakepervX(), 0)
        G.Set_Board_mat(self.Get_snakeY(), self.Get_snakeX(), 1)

    
    def Draw_Cell(self, screen: pygame.Surface):
        screen.blit(self.picture,((self.Get_snakeX())*31+1,(self.Get_snakeY()*31)+66))

    def Change_pos(self,change, G: Global.Global, keypressed, GM):
        self.Set_snakepervX(self.Get_snakeX())
        self.Set_snakepervY(self.Get_snakeY())
        self.Set_pervPic(self.Get_picture())
        board = G.Get_Board_mat()
        if(change == 1 and keypressed != 3):
            self.Set_snakeY(self.Get_snakeY() - self.snake_dy)
            GM.Set_LastkeyPressed(change)

        elif(change == 2 and keypressed != 4):
            self.Set_snakeX(self.Get_snakeX() - self.snake_dx)
            GM.Set_LastkeyPressed(change)

        elif(change == 3 and keypressed != 1):
            self.Set_snakeY(self.Get_snakeY() + self.snake_dy)
            GM.Set_LastkeyPressed(change)

        elif(change == 4 and keypressed != 2):
            self.Set_snakeX(self.Get_snakeX() + self.snake_dx)
            GM.Set_LastkeyPressed(change)
        if(self.Get_snakeX() < 0 or self.Get_snakeX() > 11 or self.Get_snakeY() < 0 or self.Get_snakeY() > 13):
            GM.P_Lose()
            return False
        G.Set_Board_mat(self.Get_snakepervY(), self.Get_snakepervX(), 0)
        G.Set_Board_mat(self.Get_snakeY(), self.Get_snakeX(), 3)

    def Is_Head(self):
        return self.Head
    

    