import pygame

class Score:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.scoreValue = 0
        self.text = self.font.render('Score: ' + str(self.scoreValue),True,(255,255,255))
        self.textRect = self.text.get_rect()

    def Get_score(self):
        return self.scoreValue
    
    def Update_Score(self):
        self.scoreValue += 1
        self.text = self.font.render('Score: ' + str(self.scoreValue),True,(255,255,255))
        self.textRect = self.text.get_rect()
    
    def Draw_score(self, screen: pygame.Surface):
        screen.blit(self.text, self.textRect)

