import Game_Manager as Game_M
import Snake


class Collisions:

    def __init__(self):
        self.Xedge = 373
        self.Yedge = 500
        pass

    def Check_P(self,Snake_Head:Snake.Snake):
        #Return True if the Player is out of bounds and False if not
        if((Snake_Head.Get_snakeX())*31+1 < 0 or (Snake_Head.Get_snakeX())*31+1 > self.Xedge):
            return True
        elif((Snake_Head.Get_snakeY()*31)+66 < 66 or (Snake_Head.Get_snakeY()*31)+66 > self.Yedge):
            return True
        return False

