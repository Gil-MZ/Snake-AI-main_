
import Snake as S

class Global:
    def __init__(self):
        #Variables:
        self.ROWS = 10
        self.COLUMNS = 10
        self.Snake_Length = 2
        #self.Snake_Cells = deque()
        self.Snake_Cells = []
        self.Board_mat = [[0 for y in range (self.COLUMNS)]for x in range (self.ROWS)]


    #Functions:
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

    def Insert_Head(self, S_Cell):
        self.Snake_Cells.insert(0,S_Cell)
        self.Set_Board_mat(S_Cell.Get_snakeX(),S_Cell.Get_snakeY(), 1)
  
    def Remove_tail(self):
        S_Cell = self.Snake_Cells.pop()
        self.Set_Board_mat(S_Cell.Get_snakeX(),S_Cell.Get_snakeY(), 0)
    
    def Get_head(self):
        return self.Snake_Cells[0]
