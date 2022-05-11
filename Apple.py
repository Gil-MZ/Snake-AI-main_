import pygame, Global_Var as Global, random

class Apple:

    def __init__(self):
        self.picture = pygame.image.load("Snake_ai Pic\Apple.png")
        self.AppleX = 0
        self.AppleY = 0
    
    def Random_place(self, screen: pygame.Surface, G: Global.Global):
        X = random.randint(0,11) 
        Y = random.randint(0,13) 
        Board = G.Get_Board_mat()
        while(X > 11 and Y > 12 and Board[X][Y] != 0):
            X = random.randint(0,13) 
            Y = random.randint(0,11)
        self.AppleX = X
        self.AppleY = Y
        G.Set_Board_mat(Y,X,2)
    
    def Draw_Apple(self, screen: pygame.Surface):
        screen.blit(self.picture, ((self.AppleX*31) + 1, (self.AppleY*31) + 66))

    def Apple_Exist(self, G: Global.Global):
        Board = G.Get_Board_mat()
        for x in range(G.ROWS):
            for y in range(G.COLUMNS):
                if(Board[x][y] == 2):
                    return True
        return False
