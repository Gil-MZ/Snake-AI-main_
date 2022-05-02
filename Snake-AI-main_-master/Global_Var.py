from collections import deque
from tkinter.tix import COLUMN
import Snake as S

class Global:
    def __init__(self):
        #Variables:
        self.WIDTH = 800
        self.HEIGHT = 600
        self.ROWS = 14
        self.COLUMNS = 12
        self.Snake_Length = 0
        self.Snake_Cells = deque()
        self.Board_mat = [[0 for y in range (self.COLUMNS)]for x in range (self.ROWS)]


    #Functions:
    def Get_Distance(self):
        return self.Snake_Distance

    def Get_ROWS(self):
        return self.ROWS
    
    def Get_Columns(self):
        return self.COLUMNS

    def Update_SnakeLength(self):
        self.Snake_Length += 1
    
    def Get_SnakeLength(self):
        return self.Snake_Length

    def Get_snakeCells(self):
        return self.Snake_Cells

    def Get_Board_mat(self):
        return self.Board_mat

    def Set_Board_mat(self, x, y, num):
        self.Board_mat[int(x)][int(y)] = num
            

    def Get_Width(self):
        return self.WIDTH

    def Get_Height(self):
        return self.HEIGHT

    def Get_Height(self):
        return self.Board_mat

    def Set_Snake_cells(self, S_Cell):
        self.Snake_Cells.append(S_Cell)
    
    def Set_Snake_cells_Right(self,S_Cell):
        self.Snake_Cells.appendleft(S_Cell)
