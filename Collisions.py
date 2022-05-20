import Global_Var


class Collisions:

    def __init__(self):
        pass

    def Check_Ai(self,X,Y,G:Global_Var.Global):
        #Return True if the Ai is out of bounds or on himself and False if not
        board = G.Get_Board_mat()
        if X < 0 or X > 9 or Y < 0 or Y > 9 or board[X][Y] == 1:
            return True
        return False
