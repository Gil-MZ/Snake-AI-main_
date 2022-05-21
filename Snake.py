import pygame, Global_Var as Global
import Collisions
import Game_Manager as Game_M

class Snake:    
    def __init__(self, picture):
        #Initializing snake variables
        self.picture = picture
        self.prevPic = None
        self.snake_X = 0
        self.snake_Y = 0
        self.snake_dx = 1
        self.snake_dy = 1

#Get functions    
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

    
    def Draw_Cell(self, screen: pygame.Surface):
        screen.blit(self.picture,((self.Get_snakeX())*31+1,(self.Get_snakeY()*31)+66))

    
    def Change_pos(self, G: Global.Global, Ai_move, GM):
        X,Y = self.Get_snakeX(),self.Get_snakeY()
        G.Board_mat
        last_mov = None
        if(Ai_move == Game_M.Direction[1] and GM.LastKeypressed != 0):#DOWN
            last_mov = 1
            #print("DOWN\n")
            Y = Y + self.snake_dy

        elif(Ai_move == Game_M.Direction[3] and GM.LastKeypressed != 2):#RIGHT
            last_mov = 3
            #print("RIGHT\n")
            X = X + self.snake_dx

        elif(Ai_move == Game_M.Direction[0] and GM.LastKeypressed != 1):#UP
            last_mov = 0
            #print("UP\n")
            Y = Y - self.snake_dy

        elif(Ai_move == Game_M.Direction[2] and GM.LastKeypressed != 3):#LEFT
            last_mov = 2
            #print("LEFT")
            X = X - self.snake_dx
        else:
            if(Game_M.Direction[0] == Game_M.Direction[GM.LastKeypressed]):
                last_mov = 0
                #print("UP\n")
                Y = Y - self.snake_dy
            elif(Game_M.Direction[1] == Game_M.Direction[GM.LastKeypressed]):
                last_mov = 1
                #print("DOWN\n")
                Y = Y + self.snake_dy
            elif(Game_M.Direction[2] == Game_M.Direction[GM.LastKeypressed]):
                last_mov = 2
                #print("LEFT")
                X = X - self.snake_dx
            elif(Game_M.Direction[3] == Game_M.Direction[GM.LastKeypressed]):
                last_mov = 3
                #print("RIGHT\n")
                X = X + self.snake_dx
        C = Collisions.Collisions()
        if(C.Check_Ai(X,Y,G)):
            GM.P_Lose()
            return False
        GM.Set_LastkeyPressed(last_mov)
        GM.Enter_snakeCell(X,Y,self.Get_picture())

    

    