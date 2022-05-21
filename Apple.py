import pygame, Global_Var as Global, random

class Apple:

    def __init__(self):
        self.picture = pygame.image.load("Snake_ai Pic\Apple.png")
        self.G = Global.Global()
        self.Apple_Places = []
        self.apple_index = 0
        self.current_apple = 0
    
    def Apples_Place(self):
        for _ in range (self.G.Get_ROWS()*self.G.Get_Columns()):
            X = random.randint(0,9) 
            Y = random.randint(0,9)
            while(self.Apple_Places.count((X,Y)) != 0):
                X = random.randint(0,9) 
                Y = random.randint(0,9)
            self.Apple_Places.append((X,Y))
    
    def reset(self):
        self.apple_index = 0
        self.current_apple = 0

    def Get_pos(self):
        return self.Apple_Places[self.current_apple]

    def Get_apple(self,G: Global.Global):
        Board = G.Get_Board_mat()
        self.current_apple = self.apple_index
        if(Board[self.Apple_Places[self.apple_index][0]][self.Apple_Places[self.apple_index][1]] != 1):
            self.apple_index += 1
        else:
            while(Board[self.Apple_Places[self.current_apple][0]][self.Apple_Places[self.current_apple][1]] == 1):
                self.current_apple += 1
        G.Set_Board_mat(self.Apple_Places[self.current_apple][0],self.Apple_Places[self.current_apple][1],2)

    #def Random_place(self, G: Global.Global):
    #    X = random.randint(0,11) 
    #    Y = random.randint(0,13) 
    #    Board = G.Get_Board_mat()
    #    while(X > 11 and Y > 12 and Board[X][Y] != 0):
    #        X = random.randint(0,13) 
    #        Y = random.randint(0,11)
    #    self.AppleX = X
    #    self.AppleY = Y
    #    G.Set_Board_mat(Y,X,2)
    
    def Draw_Apple(self, screen: pygame.Surface):
        screen.blit(self.picture, ((self.Apple_Places[self.current_apple][0]*31) + 1, (self.Apple_Places[self.current_apple][1]*31) + 66))

    def Apple_Exist(self, G: Global.Global):
        Board = G.Get_Board_mat()
        if(Board[self.Apple_Places[self.current_apple][0]][self.Apple_Places[self.current_apple][1]] == 2):
            return True
        return False
