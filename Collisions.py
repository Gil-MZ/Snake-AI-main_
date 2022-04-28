import Game_Manager as Game_M
import Snake


class Collisions:

    def __init__(self):
        pass

    def Check_P(self,Snake_Head:Snake.Snake):
        #Return True if the Player is out of bounds and False if not
        if(Snake_Head.Get_snakeX() < 0 or Snake_Head.Get_snakeX() > 373):
            return True
        elif(Snake_Head.Get_snakeY() < 66 or Snake_Head.Get_snakeY() > 500):
            return True
        return False

