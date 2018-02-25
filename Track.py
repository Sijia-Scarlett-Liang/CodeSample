
class Point:
    """
    Point: mapping the coordinate (x, y) of the 14*14 chessboard to pixel coordinate(pixel_x, pixel_y)

    Attributes:
    int x: an interger representing the row number of a chess on the 14*14 chessboard.
    int y: an interger representing the column number of a chess on the 14*14 chessboard.
    int pixel_x: an integer standing for the pixel coordinate in row with range of [30, 450].
    int pixel_y: an integer standing for the pixel coordinate in column with range of [30, 450].

    return: None
    """
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.pixel_x = 30 + 30 * self.x
        self.pixel_y = 30 + 30 * self.y


class Track_Record:

    """
    Track_Record: tracking chessboard record.
    """
    def __init__(self):
        """
        Define the initial status of chessboard.
        This is a 14*14 chessbroad. 

        Attributes:
        int count: an integer that is the initial number of step.
        records: an array that represent the chessbroad grid [0, 14]*[0, 14]. It uses to store game information: the color of chess placing on such coordiate and the current number of steps. The information will be used to check win conditions. 
        """
        self.count = 0
        self.records = [[None for i in range(15)] for j in range(15)]

    def has_record(self, x, y):
        """
        has_record: record the coordinates that are placed with chess. 

        Args:
        int x: an integer standing for the row number on the chessbroad grid.
        int y: an integer standing for the coloum number on the chessbroad grid.

        returns: a boolean. True if such coordinate has a chess, otherwise False.

        """
        return not self.records[x][y] == None

    def insert_record(self, x, y):
        '''
        insert_record: insert information about the color of a chess and the current number of step. 

        Args:
        int x: an integer standing for the row number on the chessbroad grid.
        int y: an integer standing for the coloum number on the chessbroad grid.
        int count: tracking the total number of steps with integer default as 0.
        array records[x][y]: 

        return: none
        '''
        self.count += 1
        self.records[x][y] = Step_Record(self.count)
        

    def player(self):
        '''
        player: track who places the last chess. 

        return: 1 or 2. Black is represented as 1. White is represented as 2. 
        '''
        return (self.count+1) % 2 + 1

    def check(self):
        '''
        check: check the entire chessbroad if 5 same-colored chess are in one column, one row, one right diagonal or one left diagonal.

        return: 1(black win) or 2(white win)
        '''

        '''
        column-wise checking. check black chess firstly and then white chess.
        '''
        for x in range(15):
            for y in range(11): 
                 if self.has_record(x, y) and self.has_record(x, y+1) and self.has_record(x, y+2) and self.has_record(x, y+3) and self.has_record(x, y+4):
                    if self.records[x][y].color == 1 and self.records[x][y+1].color == 1 and self.records[x][y+2].color == 1 and self.records[x][y+3].color == 1 and self.records[x][y+4].color == 1:
                        result = 1
                        return result
                        break
                    elif self.records[x][y].color == 2 and self.records[x][y+1].color == 2 and self.records[x][y+2].color == 2 and self.records[x][y+3].color == 2 and self.records[x][y+4].color == 2:
                        result = 2
                        return result
                        break
                    else:
                        result = 0
        '''
        row-wise checking.
        '''
        for x in range(11):
            for y in range(15):         
                if self.has_record(x, y) and self.has_record(x+1, y) and self.has_record(x+2, y) and self.has_record(x+3, y) and self.has_record(x+4, y):
                    if self.records[x][y].color == 1 and self.records[x+1][y].color == 1 and self.records[x+2][y].color == 1 and self.records[x+3][y].color == 1 and self.records[x+4][y].color == 1:
                        result = 1
                        return result
                        break
                    elif self.records[x][y].color == 2 and self.records[x+1][y].color == 2 and self.records[x+2][y].color == 2 and self.records[x+3][y].color == 2 and self.records[x+4][y].color == 2:
                        result = 2
                        return result
                        break
                    else:
                        result = 0
        '''
        right diagonal checking.
        '''
        for x in range(11):
            for y in range(11):
                if self.has_record(x, y) and self.has_record(x+1, y+1) and self.has_record(x+2, y+2) and self.has_record(x+3, y+3) and self.has_record(x+4, y+4):
                    if self.records[x][y].color == 1 and self.records[x+1][y+1].color == 1 and self.records[x+2][y+2].color == 1 and self.records[x+3][y+3].color == 1 and self.records[x+4][y+4].color == 1:
                        result = 1
                        return result
                        break
                    elif self.records[x][y].color == 2 and self.records[x+1][y+1].color == 2 and self.records[x+2][y+2].color == 2 and self.records[x+3][y+3].color == 2 and self.records[x+4][y+4].color == 2:
                        result = 2
                        return result    
                        break
                    else:
                        result = 0
        '''
        left diagonal checking.
        '''
        for x in range(11):
            for y in range(4, 15):
                if self.has_record(x, y) and self.has_record(x+1, y-1) and self.has_record(x+2, y-2) and self.has_record(x+3, y-3) and self.has_record(x+4, y-4):
                    if self.records[x][y].color == 1 and self.records[x+1][y-1].color == 1 and self.records[x+2][y-2].color == 1 and self.records[x+3][y-3].color == 1 and self.records[x+4][y-4].color == 1:
                        result = 1
                        return result
                        break

                    elif self.records[x][y].color == 2 and self.records[x+1][y-1].color == 2 and self.records[x+2][y-2].color == 2 and self.records[x+3][y-3].color == 2 and self.records[x+4][y-4].color == 2:
                        result = 2
                        return result
                        break
                    else:
                        result = 0


class Step_Record:
    """
    Step_Record: tracking the number of steps that two plays place on the chessbroad.

    Attributes:
    int count: an integer tracking the total number of steps with integer default as 1.
    int color: a binary index tracking the color of the last chess placing on the chessbroad.
    Black is represented as 1. White is represented as 2.   

    Return: None
    """
    def __init__(self, count):
        self.count = count
        self.color = (self.count+1) % 2 + 1