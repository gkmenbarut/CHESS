class Chess_Board:
    def __init__(self):
        self.board = self.create_board()
        
    def create_board(self):
        board_x=[]

        for x in range(8):
            board_y =[]
            for y in range(8):
                

                board_y.append('.')

            board_x.append(board_y)

        board_x[7][4] = 'K'
        board_x[7][3] = 'Q'
        board_x[7][2] = 'B'
        board_x[7][1] = 'N'
        board_x[7][0] = 'R'
        board_x[7][6] = 'N'
        board_x[7][7] = 'R'
        board_x[7][5] = 'B'
        board_x[0][4] = 'K'
        board_x[0][0] = 'R'
        board_x[0][1] = 'N'
        board_x[0][2] = 'B'
        board_x[0][3] = 'Q'
        board_x[0][7] = 'R'
        board_x[0][6] = 'N'
        board_x[0][5] = 'B'
        board_x[6][5] = 'P'
        board_x[6][4] = 'P'
        board_x[6][3] = 'P'
        board_x[6][2] = 'P'
        board_x[6][1] = 'P'
        board_x[6][0] = 'P'
        board_x[6][6] = 'P'
        board_x[6][7] = 'P'
        board_x[1][7] = 'P'
        board_x[1][6] = 'P'
        board_x[1][5] = 'P'
        board_x[1][4] = 'P'
        board_x[1][3] = 'P'
        board_x[1][2] = 'P'
        board_x[1][1] = 'P'
        board_x[1][0] = 'P'
        return board_x

        

        
class BLACK_PAWN_7(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_bp_7 = 1
        self.position_y_bp_7 = 7
        self.symbol_bp_7 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for black_pawn_7',(self.position_x_bp_7,self.position_y_bp_7))
                destination_x_bp_7 = int(input('row:'))
                destination_y_bp_7= int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  

                    if self.board[destination_x_bp_7][destination_y_bp_7] == '.' :

                        if abs(self.position_x_bp_7-destination_x_bp_7) == 1 and abs(self.position_y_bp_7-destination_y_bp_7) == 0 :
                            self.board[self.position_x_bp_7][self.position_y_bp_7] = '.'
                            self.position_x_bp_7 = destination_x_bp_7
                            self.position_y_bp_7 = destination_y_bp_7
                            self.board[self.position_x_bp_7][self.position_y_bp_7] = self.symbol_bp_7
                        
                            return self.board
                            break
                        
                        elif (self.position_x_bp_7,self.position_y_bp_7) == (1,0):
                            if abs(self.position_x_bp_7-destination_x_bp_7) == 2 and abs(self.position_y_bp_7-destination_y_bp_7) == 0 :
                                self.board[self.position_x_bp_7][self.position_y_bp_7] = '.'
                                self.position_x_bp_7 = destination_x_bp_7
                                self.position_y_bp_7 = destination_y_bp_7
                                self.board[self.position_x_bp_7][self.position_y_bp_7] = self.symbol_bp_7
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_bp_7][destination_y_bp_7] != '.' :
                            if self.board[destination_x_bp_7][destination_y_bp_7] == self.board[self.position_x_bp_7-1][self.position_y_bp_7-1]:
                                self.board[self.position_x_bp_7][self.position_y_bp_7] = '.'
                                self.position_x_bp_7 = destination_x_bp_7
                                self.position_y_bp_7 = destination_y_bp_7
                                self.board[self.position_x_bp_7][self.position_y_bp_7] = self.symbol_bp_7
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_bp_7][destination_y_bp_7] == self.board[self.position_x_bp_7-1][self.position_y_bp_7+1]:
                                self.board[self.position_x_bp_7][self.position_y_bp_7] = '.'
                                self.position_x_bp_7 = destination_x_bp_7
                                self.position_y_bp_7 = destination_y_bp_7
                                self.board[self.position_x_bp_7][self.position_y_bp_7] = self.symbol_bp_7
                        
                                return self.board
                                break
                        continue
            except:
                pass


class BLACK_PAWN_6(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_bp_6 = 1
        self.position_y_bp_6 = 6
        self.symbol_bp_6 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for black_pawn_6',(self.position_x_bp_6,self.position_y_bp_6))
                destination_x_bp_6 = int(input('row:'))
                destination_y_bp_6= int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_bp_6][destination_y_bp_6] == '.' :

                        if abs(self.position_x_bp_6-destination_x_bp_6) == 1 and abs(self.position_y_bp_6-destination_y_bp_6) == 0 :
                            self.board[self.position_x_bp_6][self.position_y_bp_6] = '.'
                            self.position_x_bp_6 = destination_x_bp_6
                            self.position_y_bp_6 = destination_y_bp_6
                            self.board[self.position_x_bp_6][self.position_y_bp_6] = self.symbol_bp_6
                        
                            return self.board
                            break
                        
                        elif (self.position_x_bp_6,self.position_y_bp_6) == (1,6):
                            if abs(self.position_x_bp_6-destination_x_bp_6) == 2 and abs(self.position_y_bp_6-destination_y_bp_6) == 0 :
                                self.board[self.position_x_bp_6][self.position_y_bp_6] = '.'
                                self.position_x_bp_6 = destination_x_bp_6
                                self.position_y_bp_6 = destination_y_bp_6
                                self.board[self.position_x_bp_6][self.position_y_bp_6] = self.symbol_bp_6
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_bp_6][destination_y_bp_6] != '.' :
                            if self.board[destination_x_bp_6][destination_y_bp_6] == self.board[self.position_x_bp_6-1][self.position_y_bp_6-1]:
                                self.board[self.position_x_bp_6][self.position_y_bp_6] = '.'
                                self.position_x_bp_6 = destination_x_bp_6
                                self.position_y_bp_6 = destination_y_bp_6
                                self.board[self.position_x_bp_6][self.position_y_bp_6] = self.symbol_bp_6
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_bp_6][destination_y_bp_6] == self.board[self.position_x_bp_6-1][self.position_y_bp_6+1]:
                                self.board[self.position_x_bp_6][self.position_y_bp_6] = '.'
                                self.position_x_bp_6 = destination_x_bp_6
                                self.position_y_bp_6 = destination_y_bp_6
                                self.board[self.position_x_bp_6][self.position_y_bp_6] = self.symbol_bp_6
                        
                                return self.board
                                break
                        continue
            except:
                pass
    
class BLACK_PAWN_5(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_bp_5 = 1
        self.position_y_bp_5 = 5
        self.symbol_bp_5 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for black_pawn_5',(self.position_x_bp_5,self.position_y_bp_5))
                destination_x_bp_5 = int(input('row:'))
                destination_y_bp_5 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_bp_5][destination_y_bp_5] == '.' :

                        if abs(self.position_x_bp_5-destination_x_bp_5) == 1 and abs(self.position_y_bp_5-destination_y_bp_5) == 0 :
                            self.board[self.position_x_bp_5][self.position_y_bp_5] = '.'
                            self.position_x_bp_5 = destination_x_bp_5
                            self.position_y_bp_5 = destination_y_bp_5
                            self.board[self.position_x_bp_5][self.position_y_bp_5] = self.symbol_bp_5
                        
                            return self.board
                            break
                        
                        elif (self.position_x_bp_5,self.position_y_bp_5) == (1,5):
                            if abs(self.position_x_bp_5-destination_x_bp_5) == 2 and abs(self.position_y_bp_5-destination_y_bp_5) == 0 :
                                self.board[self.position_x_bp_5][self.position_y_bp_5] = '.'
                                self.position_x_bp_5 = destination_x_bp_5
                                self.position_y_bp_5 = destination_y_bp_5
                                self.board[self.position_x_bp_5][self.position_y_bp_5] = self.symbol_bp_5
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_bp_5][destination_y_bp_5] != '.' :
                            if self.board[destination_x_bp_5][destination_y_bp_5] == self.board[self.position_x_bp_5-1][self.position_y_bp_5-1]:
                                self.board[self.position_x_bp_5][self.position_y_bp_5] = '.'
                                self.position_x_bp_5 = destination_x_bp_5
                                self.position_y_bp_5 = destination_y_bp_5
                                self.board[self.position_x_bp_5][self.position_y_bp_5] = self.symbol_bp_5
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_bp_5][destination_y_bp_5] == self.board[self.position_x_bp_5-1][self.position_y_bp_5+1]:
                                self.board[self.position_x_bp_5][self.position_y_bp_5] = '.'
                                self.position_x_bp_5 = destination_x_bp_5
                                self.position_y_bp_5 = destination_y_bp_5
                                self.board[self.position_x_bp_5][self.position_y_bp_5] = self.symbol_bp_5
                        
                                return self.board
                                break
                        continue
            except:
                pass


class BLACK_PAWN_0(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_bp_0 = 1
        self.position_y_bp_0 = 0
        self.symbol_bp_0 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for black_pawn_0',(self.position_x_bp_0,self.position_y_bp_0))
                destination_x_bp_0 = int(input('row:'))
                destination_y_bp_0= int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_bp_0][destination_y_bp_0] == '.' :

                        if abs(self.position_x_bp_0-destination_x_bp_0) == 1 and abs(self.position_y_bp_0-destination_y_bp_0) == 0 :
                            self.board[self.position_x_bp_0][self.position_y_bp_0] = '.'
                            self.position_x_bp_0 = destination_x_bp_0
                            self.position_y_bp_0 = destination_y_bp_0
                            self.board[self.position_x_bp_0][self.position_y_bp_0] = self.symbol_bp_0
                        
                            return self.board
                            break
                        
                        elif (self.position_x_bp_0,self.position_y_bp_0) == (1,0):
                            if abs(self.position_x_bp_0-destination_x_bp_0) == 2 and abs(self.position_y_bp_0-destination_y_bp_0) == 0 :
                                self.board[self.position_x_bp_0][self.position_y_bp_0] = '.'
                                self.position_x_bp_0 = destination_x_bp_0
                                self.position_y_bp_0 = destination_y_bp_0
                                self.board[self.position_x_bp_0][self.position_y_bp_0] = self.symbol_bp_0
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_bp_0][destination_y_bp_0] != '.' :
                            if self.board[destination_x_bp_0][destination_y_bp_0] == self.board[self.position_x_bp_0-1][self.position_y_bp_0-1]:
                                self.board[self.position_x_bp_0][self.position_y_bp_0] = '.'
                                self.position_x_bp_0 = destination_x_bp_0
                                self.position_y_bp_0 = destination_y_bp_0
                                self.board[self.position_x_bp_0][self.position_y_bp_0] = self.symbol_bp_0
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_bp_0][destination_y_bp_0] == self.board[self.position_x_bp_0-1][self.position_y_bp_0+1]:
                                self.board[self.position_x_bp_0][self.position_y_bp_0] = '.'
                                self.position_x_bp_0 = destination_x_bp_0
                                self.position_y_bp_0 = destination_y_bp_0
                                self.board[self.position_x_bp_0][self.position_y_bp_0] = self.symbol_bp_0
                        
                                return self.board
                                break
                        continue
            except:
                pass

class BLACK_PAWN_1(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_bp_1 = 1
        self.position_y_bp_1 = 1
        self.symbol_bp_1 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for black_pawn_1',(self.position_x_bp_1,self.position_y_bp_1))
                destination_x_bp_1 = int(input('row:'))
                destination_y_bp_1= int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_bp_1][destination_y_bp_1] == '.' :

                        if abs(self.position_x_bp_1-destination_x_bp_1) == 1 and abs(self.position_y_bp_1-destination_y_bp_1) == 0 :
                            self.board[self.position_x_bp_1][self.position_y_bp_1] = '.'
                            self.position_x_bp_1 = destination_x_bp_1
                            self.position_y_bp_1 = destination_y_bp_1
                            self.board[self.position_x_bp_1][self.position_y_bp_1] = self.symbol_bp_1
                        
                            return self.board
                            break
                        
                        elif (self.position_x_bp_1,self.position_y_bp_1) == (1,1):
                            if abs(self.position_x_bp_1-destination_x_bp_1) == 2 and abs(self.position_y_bp_1-destination_y_bp_1) == 0 :
                                self.board[self.position_x_bp_1][self.position_y_bp_1] = '.'
                                self.position_x_bp_1 = destination_x_bp_1
                                self.position_y_bp_1 = destination_y_bp_1
                                self.board[self.position_x_bp_1][self.position_y_bp_1] = self.symbol_bp_1
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_bp_1][destination_y_bp_1] != '.' :
                            if self.board[destination_x_bp_1][destination_y_bp_1] == self.board[self.position_x_bp_1-1][self.position_y_bp_1-1]:
                                self.board[self.position_x_bp_1][self.position_y_bp_1] = '.'
                                self.position_x_bp_1 = destination_x_bp_1
                                self.position_y_bp_1 = destination_y_bp_1
                                self.board[self.position_x_bp_1][self.position_y_bp_1] = self.symbol_bp_1
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_bp_1][destination_y_bp_1] == self.board[self.position_x_bp_1-1][self.position_y_bp_1+1]:
                                self.board[self.position_x_bp_1][self.position_y_bp_1] = '.'
                                self.position_x_bp_1 = destination_x_bp_1
                                self.position_y_bp_1 = destination_y_bp_1
                                self.board[self.position_x_bp_1][self.position_y_bp_1] = self.symbol_bp_1
                        
                                return self.board
                                break
                        continue
            except:
                pass

class BLACK_PAWN_2(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_bp_2 = 1
        self.position_y_bp_2 = 2
        self.symbol_bp_2 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for black_pawn_2',(self.position_x_bp_2,self.position_y_bp_2))
                
                destination_x_bp_2 = int(input('row:'))
                destination_y_bp_2= int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_bp_2][destination_y_bp_2] == '.' :

                        if abs(self.position_x_bp_2-destination_x_bp_2) == 1 and abs(self.position_y_bp_2-destination_y_bp_2) == 0 :
                            self.board[self.position_x_bp_2][self.position_y_bp_2] = '.'
                            self.position_x_bp_2 = destination_x_bp_2
                            self.position_y_bp_2 = destination_y_bp_2
                            self.board[self.position_x_bp_2][self.position_y_bp_2] = self.symbol_bp_2
                        
                            return self.board
                            break
                        
                        elif (self.position_x_bp_2,self.position_y_bp_2) == (1,2):
                            if abs(self.position_x_bp_2-destination_x_bp_2) == 2 and abs(self.position_y_bp_2-destination_y_bp_2) == 0 :
                                self.board[self.position_x_bp_2][self.position_y_bp_2] = '.'
                                self.position_x_bp_2 = destination_x_bp_2
                                self.position_y_bp_2 = destination_y_bp_2
                                self.board[self.position_x_bp_2][self.position_y_bp_2] = self.symbol_bp_2
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_bp_2][destination_y_bp_2] != '.' :
                            if self.board[destination_x_bp_2][destination_y_bp_2] == self.board[self.position_x_bp_2-1][self.position_y_bp_2-1]:
                                self.board[self.position_x_bp_2][self.position_y_bp_2] = '.'
                                self.position_x_bp_2 = destination_x_bp_2
                                self.position_y_bp_2 = destination_y_bp_2
                                self.board[self.position_x_bp_2][self.position_y_bp_2] = self.symbol_bp_2
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_bp_2][destination_y_bp_2] == self.board[self.position_x_bp_2-1][self.position_y_bp_2+1]:
                                self.board[self.position_x_bp_2][self.position_y_bp_2] = '.'
                                self.position_x_bp_2 = destination_x_bp_2
                                self.position_y_bp_2 = destination_y_bp_2
                                self.board[self.position_x_bp_2][self.position_y_bp_2] = self.symbol_bp_2
                        
                                return self.board
                                break
                        continue
            except:
                pass

class BLACK_PAWN_3(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_bp_3 = 1
        self.position_y_bp_3 = 3
        self.symbol_bp_3 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for black_pawn_3',(self.position_x_bp_3,self.position_y_bp_3))
                destination_x_bp_3 = int(input('row:'))
                destination_y_bp_3 = int(input('column:'))
                
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_bp_3][destination_y_bp_3] == '.' :

                        if abs(self.position_x_bp_3-destination_x_bp_3) == 1 and abs(self.position_y_bp_3-destination_y_bp_3) == 0 :
                            self.board[self.position_x_bp_3][self.position_y_bp_3] = '.'
                            self.position_x_bp_3 = destination_x_bp_3
                            self.position_y_bp_3 = destination_y_bp_3
                            self.board[self.position_x_bp_3][self.position_y_bp_3] = self.symbol_bp_3
                        
                            return self.board
                            break
                        
                        elif (self.position_x_bp_3,self.position_y_bp_3) == (1,3):
                            if abs(self.position_x_bp_3-destination_x_bp_3) == 2 and abs(self.position_y_bp_3-destination_y_bp_3) == 0 :
                                self.board[self.position_x_bp_3][self.position_y_bp_3] = '.'
                                self.position_x_bp_3 = destination_x_bp_3
                                self.position_y_bp_3 = destination_y_bp_3
                                self.board[self.position_x_bp_3][self.position_y_bp_3] = self.symbol_bp_3
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_bp_3][destination_y_bp_3] != '.' :
                            if self.board[destination_x_bp_3][destination_y_bp_3] == self.board[self.position_x_bp_3-1][self.position_y_bp_3-1]:
                                self.board[self.position_x_bp_3][self.position_y_bp_3] = '.'
                                self.position_x_bp_3 = destination_x_bp_3
                                self.position_y_bp_3 = destination_y_bp_3
                                self.board[self.position_x_bp_3][self.position_y_bp_3] = self.symbol_bp_3
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_bp_3][destination_y_bp_3] == self.board[self.position_x_bp_3-1][self.position_y_bp_3+1]:
                                self.board[self.position_x_bp_3][self.position_y_bp_3] = '.'
                                self.position_x_bp_3 = destination_x_bp_3
                                self.position_y_bp_3 = destination_y_bp_3
                                self.board[self.position_x_bp_3][self.position_y_bp_3] = self.symbol_bp_3
                        
                                return self.board
                                break
                        
                        continue
            except:
                pass

class BLACK_PAWN_4(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_bp_4 = 1
        self.position_y_bp_4 = 4
        self.symbol_bp_4 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for black_pawn_4',(self.position_x_bp_4,self.position_y_bp_4))
                destination_x_bp_4 = int(input('row:'))
                destination_y_bp_4 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_bp_4][destination_y_bp_4] == '.' :

                        if abs(self.position_x_bp_4-destination_x_bp_4) == 1 and abs(self.position_y_bp_4-destination_y_bp_4) == 0 :
                            self.board[self.position_x_bp_4][self.position_y_bp_4] = '.'
                            self.position_x_bp_4 = destination_x_bp_4
                            self.position_y_bp_4 = destination_y_bp_4
                            self.board[self.position_x_bp_4][self.position_y_bp_4] = self.symbol_bp_4
                        
                            return self.board
                            break
                        
                        elif (self.position_x_bp_4,self.position_y_bp_4) == (1,4):
                            if abs(self.position_x_bp_4-destination_x_bp_4) == 2 and abs(self.position_y_bp_4-destination_y_bp_4) == 0 :
                                self.board[self.position_x_bp_4][self.position_y_bp_4] = '.'
                                self.position_x_bp_4 = destination_x_bp_4
                                self.position_y_bp_4 = destination_y_bp_4
                                self.board[self.position_x_bp_4][self.position_y_bp_4] = self.symbol_bp_4
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_bp_4][destination_y_bp_4] != '.' :
                            if self.board[destination_x_bp_4][destination_y_bp_4] == self.board[self.position_x_bp_4-1][self.position_y_bp_4-1]:
                                self.board[self.position_x_bp_4][self.position_y_bp_4] = '.'
                                self.position_x_bp_4 = destination_x_bp_4
                                self.position_y_bp_4 = destination_y_bp_4
                                self.board[self.position_x_bp_4][self.position_y_bp_4] = self.symbol_bp_4
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_bp_4][destination_y_bp_4] == self.board[self.position_x_bp_4-1][self.position_y_bp_4+1]:
                                self.board[self.position_x_bp_4][self.position_y_bp_4] = '.'
                                self.position_x_bp_4 = destination_x_bp_4
                                self.position_y_bp_4 = destination_y_bp_4
                                self.board[self.position_x_bp_4][self.position_y_bp_4] = self.symbol_bp_4
                        
                                return self.board
                                break
                        continue
            except:
                pass

class WHITE_PAWN_7(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_p_7 = 6
        self.position_y_p_7 = 7
        self.symbol_p_7 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for white_pawn_7',(self.position_x_p_7,self.position_y_p_7))
                destination_x_p_7 = int(input('row:'))
                destination_y_p_7 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_p_7][destination_y_p_7] == '.' :

                        if abs(self.position_x_p_7-destination_x_p_7) == 1 and abs(self.position_y_p_7-destination_y_p_7) == 0 :
                            self.board[self.position_x_p_7][self.position_y_p_7] = '.'
                            self.position_x_p_7 = destination_x_p_7
                            self.position_y_p_7 = destination_y_p_7
                            self.board[self.position_x_p_7][self.position_y_p_7] = self.symbol_p_7
                        
                            return self.board
                            break
                        
                        elif (self.position_x_p_7,self.position_y_p_7) == (6,7):
                            if abs(self.position_x_p_7-destination_x_p_7) == 2 and abs(self.position_y_p_7-destination_y_p_7) == 0 :
                                self.board[self.position_x_p_7][self.position_y_p_7] = '.'
                                self.position_x_p_7 = destination_x_p_7
                                self.position_y_p_7 = destination_y_p_7
                                self.board[self.position_x_p_7][self.position_y_p_7] = self.symbol_p_7
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_p_7][destination_y_p_7] != '.' :
                            if self.board[destination_x_p_7][destination_y_p_7] == self.board[self.position_x_p_7-1][self.position_y_p_7-1]:
                                self.board[self.position_x_p_7][self.position_y_p_7] = '.'
                                self.position_x_p_7 = destination_x_p_7
                                self.position_y_p_7 = destination_y_p_7
                                self.board[self.position_x_p_7][self.position_y_p_7] = self.symbol_p_7
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_p_7][destination_y_p_7] == self.board[self.position_x_p_7-1][self.position_y_p_7+1]:
                                self.board[self.position_x_p_7][self.position_y_p_7] = '.'
                                self.position_x_p_7 = destination_x_p_7
                                self.position_y_p_7 = destination_y_p_7
                                self.board[self.position_x_p_7][self.position_y_p_7] = self.symbol_p_7
                        
                                return self.board
                                break
                        continue
            except:
                pass
    
class WHITE_PAWN_6(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_p_6 = 6
        self.position_y_p_6 = 6
        self.symbol_p_6 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for white_pawn_6',(self.position_x_p_6,self.position_y_p_6))
                destination_x_p_6 = int(input('row:'))
                destination_y_p_6 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_p_6][destination_y_p_6] == '.' :

                        if abs(self.position_x_p_6-destination_x_p_6) == 1 and abs(self.position_y_p_6-destination_y_p_6) == 0 :
                            self.board[self.position_x_p_6][self.position_y_p_6] = '.'
                            self.position_x_p_6 = destination_x_p_6
                            self.position_y_p_6 = destination_y_p_6
                            self.board[self.position_x_p_6][self.position_y_p_6] = self.symbol_p_6
                        
                            return self.board
                            break
                        
                        elif (self.position_x_p_6,self.position_y_p_6) == (6,6):
                            if abs(self.position_x_p_6-destination_x_p_6) == 2 and abs(self.position_y_p_6-destination_y_p_6) == 0 :
                                self.board[self.position_x_p_6][self.position_y_p_6] = '.'
                                self.position_x_p_6 = destination_x_p_6
                                self.position_y_p_6 = destination_y_p_6
                                self.board[self.position_x_p_6][self.position_y_p_6] = self.symbol_p_6
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_p_6][destination_y_p_6] != '.' :
                            if self.board[destination_x_p_6][destination_y_p_6] == self.board[self.position_x_p_6-1][self.position_y_p_6-1]:
                                self.board[self.position_x_p_6][self.position_y_p_6] = '.'
                                self.position_x_p_6 = destination_x_p_6
                                self.position_y_p_6 = destination_y_p_6
                                self.board[self.position_x_p_6][self.position_y_p_6] = self.symbol_p_6
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_p_6][destination_y_p_6] == self.board[self.position_x_p_6-1][self.position_y_p_6+1]:
                                self.board[self.position_x_p_6][self.position_y_p_6] = '.'
                                self.position_x_p_6 = destination_x_p_6
                                self.position_y_p_6 = destination_y_p_6
                                self.board[self.position_x_p_6][self.position_y_p_6] = self.symbol_p_6
                        
                                return self.board
                                break
                        continue
            except:
                pass



class WHITE_PAWN_5(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_p_5 = 6
        self.position_y_p_5 = 5
        self.symbol_p_5 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for white_pawn_5',(self.position_x_p_5,self.position_y_p_5))
                destination_x_p_5 = int(input('row:'))
                destination_y_p_5 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_p_5][destination_y_p_5] == '.' :

                        if abs(self.position_x_p_5-destination_x_p_5) == 1 and abs(self.position_y_p_5-destination_y_p_5) == 0 :
                            self.board[self.position_x_p_5][self.position_y_p_5] = '.'
                            self.position_x_p_5 = destination_x_p_5
                            self.position_y_p_5 = destination_y_p_5
                            self.board[self.position_x_p_5][self.position_y_p_5] = self.symbol_p_5
                        
                            return self.board
                            break
                        
                        elif (self.position_x_p_5,self.position_y_p_5) == (6,5):
                            if abs(self.position_x_p_5-destination_x_p_5) == 2 and abs(self.position_y_p_5-destination_y_p_5) == 0 :
                                self.board[self.position_x_p_5][self.position_y_p_5] = '.'
                                self.position_x_p_5 = destination_x_p_5
                                self.position_y_p_5 = destination_y_p_5
                                self.board[self.position_x_p_5][self.position_y_p_5] = self.symbol_p_5
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_p_5][destination_y_p_5] != '.' :
                            if self.board[destination_x_p_5][destination_y_p_5] == self.board[self.position_x_p_5-1][self.position_y_p_5-1]:
                                self.board[self.position_x_p_5][self.position_y_p_5] = '.'
                                self.position_x_p_5 = destination_x_p_5
                                self.position_y_p_5 = destination_y_p_5
                                self.board[self.position_x_p_5][self.position_y_p_5] = self.symbol_p_5
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_p_5][destination_y_p_5] == self.board[self.position_x_p_5-1][self.position_y_p_5+1]:
                                self.board[self.position_x_p_5][self.position_y_p_5] = '.'
                                self.position_x_p_5 = destination_x_p_5
                                self.position_y_p_5 = destination_y_p_5
                                self.board[self.position_x_p_5][self.position_y_p_5] = self.symbol_p_5
                        
                                return self.board
                                break
                        continue
            except:
                pass

class WHITE_PAWN_0(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_p_0 = 6
        self.position_y_p_0 = 0
        self.symbol_p_0 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for white_pawn_0',(self.position_x_p_0,self.position_y_p_0))
                destination_x_p_0 = int(input('row:'))
                destination_y_p_0 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_p_0][destination_y_p_0] == '.' :

                        if abs(self.position_x_p_0-destination_x_p_0) == 1 and abs(self.position_y_p_0-destination_y_p_0) == 0 :
                            self.board[self.position_x_p_0][self.position_y_p_0] = '.'
                            self.position_x_p_0 = destination_x_p_0
                            self.position_y_p_0 = destination_y_p_0
                            self.board[self.position_x_p_0][self.position_y_p_0] = self.symbol_p_0
                        
                            return self.board
                            break
                        
                        elif (self.position_x_p_0,self.position_y_p_0) == (6,0):
                            if abs(self.position_x_p_0-destination_x_p_0) == 2 and abs(self.position_y_p_0-destination_y_p_0) == 0 :
                                self.board[self.position_x_p_0][self.position_y_p_0] = '.'
                                self.position_x_p_0 = destination_x_p_0
                                self.position_y_p_0 = destination_y_p_0
                                self.board[self.position_x_p_0][self.position_y_p_0] = self.symbol_p_0
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_p_0][destination_y_p_0] != '.' :
                            if self.board[destination_x_p_0][destination_y_p_0] == self.board[self.position_x_p_0-1][self.position_y_p_0-1]:
                                self.board[self.position_x_p_0][self.position_y_p_0] = '.'
                                self.position_x_p_0 = destination_x_p_0
                                self.position_y_p_0 = destination_y_p_0
                                self.board[self.position_x_p_0][self.position_y_p_0] = self.symbol_p_0
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_p_0][destination_y_p_0] == self.board[self.position_x_p_0-1][self.position_y_p_0+1]:
                                self.board[self.position_x_p_0][self.position_y_p_0] = '.'
                                self.position_x_p_0 = destination_x_p_0
                                self.position_y_p_0 = destination_y_p_0
                                self.board[self.position_x_p_0][self.position_y_p_0] = self.symbol_p_0
                        
                                return self.board
                                break
                        continue
            except:
                pass

class WHITE_PAWN_1(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_p_1 = 6
        self.position_y_p_1 = 1
        self.symbol_p_1 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for white_pawn_1',(self.position_x_p_1,self.position_y_p_1))
                destination_x_p_1 = int(input('row:'))
                destination_y_p_1 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_p_1][destination_y_p_1] == '.' :

                        if abs(self.position_x_p_1-destination_x_p_1) == 1 and abs(self.position_y_p_1-destination_y_p_1) == 0 :
                            self.board[self.position_x_p_1][self.position_y_p_1] = '.'
                            self.position_x_p_1 = destination_x_p_1
                            self.position_y_p_1 = destination_y_p_1
                            self.board[self.position_x_p_1][self.position_y_p_1] = self.symbol_p_1
                        
                            return self.board
                            break
                        
                        elif (self.position_x_p_1,self.position_y_p_1) == (6,1):
                            if abs(self.position_x_p_1-destination_x_p_1) == 2 and abs(self.position_y_p_1-destination_y_p_1) == 0 :
                                self.board[self.position_x_p_1][self.position_y_p_1] = '.'
                                self.position_x_p_1 = destination_x_p_1
                                self.position_y_p_1 = destination_y_p_1
                                self.board[self.position_x_p_1][self.position_y_p_1] = self.symbol_p_1
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_p_1][destination_y_p_1] != '.' :
                            if self.board[destination_x_p_1][destination_y_p_1] == self.board[self.position_x_p_1-1][self.position_y_p_1-1]:
                                self.board[self.position_x_p_1][self.position_y_p_1] = '.'
                                self.position_x_p_1 = destination_x_p_1
                                self.position_y_p_1 = destination_y_p_1
                                self.board[self.position_x_p_1][self.position_y_p_1] = self.symbol_p_1
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_p_1][destination_y_p_1] == self.board[self.position_x_p_1-1][self.position_y_p_1+1]:
                                self.board[self.position_x_p_1][self.position_y_p_1] = '.'
                                self.position_x_p_1 = destination_x_p_1
                                self.position_y_p_1 = destination_y_p_1
                                self.board[self.position_x_p_1][self.position_y_p_1] = self.symbol_p_1
                        
                                return self.board
                                break
                        continue
                    
            except:
                pass


class WHITE_PAWN_2(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_p_2 = 6
        self.position_y_p_2 = 2
        self.symbol_p_2 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for white_pawn_2',(self.position_x_p_2,self.position_y_p_2))
                destination_x_p_2 = int(input('row:'))
                destination_y_p_2 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_p_2][destination_y_p_2] == '.' :

                        if abs(self.position_x_p_2-destination_x_p_2) == 1 and abs(self.position_y_p_2-destination_y_p_2) == 0 :
                            self.board[self.position_x_p_2][self.position_y_p_2] = '.'
                            self.position_x_p_2 = destination_x_p_2
                            self.position_y_p_2 = destination_y_p_2
                            self.board[self.position_x_p_2][self.position_y_p_2] = self.symbol_p_2
                        
                            return self.board
                            break
                        
                        elif (self.position_x_p_2,self.position_y_p_2) == (6,2):
                            if abs(self.position_x_p_2-destination_x_p_2) == 2 and abs(self.position_y_p_2-destination_y_p_2) == 0 :
                                self.board[self.position_x_p_2][self.position_y_p_2] = '.'
                                self.position_x_p_2 = destination_x_p_2
                                self.position_y_p_2 = destination_y_p_2
                                self.board[self.position_x_p_2][self.position_y_p_2] = self.symbol_p_2
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_p_2][destination_y_p_2] != '.' :
                            if self.board[destination_x_p_2][destination_y_p_2] == self.board[self.position_x_p_2-1][self.position_y_p_2-1]:
                                self.board[self.position_x_p_2][self.position_y_p_2] = '.'
                                self.position_x_p_2 = destination_x_p_2
                                self.position_y_p_2 = destination_y_p_2
                                self.board[self.position_x_p_2][self.position_y_p_2] = self.symbol_p_2
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_p_2][destination_y_p_2] == self.board[self.position_x_p_2-1][self.position_y_p_2+1]:
                                self.board[self.position_x_p_2][self.position_y_p_2] = '.'
                                self.position_x_p_2 = destination_x_p_2
                                self.position_y_p_2 = destination_y_p_2
                                self.board[self.position_x_p_2][self.position_y_p_2] = self.symbol_p_2
                        
                                return self.board
                                break
                        continue
            except:
                pass



class WHITE_PAWN_3(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_p_3 = 6
        self.position_y_p_3 = 3
        self.symbol_p_3 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for white_pawn_3',(self.position_x_p_3,self.position_y_p_3))
                destination_x_p_3 = int(input('row:'))
                destination_y_p_3 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_p_3][destination_y_p_3] == '.' :

                        if abs(self.position_x_p_3-destination_x_p_3) == 1 and abs(self.position_y_p_3-destination_y_p_3) == 0 :
                            self.board[self.position_x_p_3][self.position_y_p_3] = '.'
                            self.position_x_p_3 = destination_x_p_3
                            self.position_y_p_3 = destination_y_p_3
                            self.board[self.position_x_p_3][self.position_y_p_3] = self.symbol_p_3
                        
                            return self.board
                            break
                        
                        elif (self.position_x_p_3,self.position_y_p_3) == (6,3):
                            if abs(self.position_x_p_3-destination_x_p_3) == 2 and abs(self.position_y_p_3-destination_y_p_3) == 0 :
                                self.board[self.position_x_p_3][self.position_y_p_3] = '.'
                                self.position_x_p_3 = destination_x_p_3
                                self.position_y_p_3 = destination_y_p_3
                                self.board[self.position_x_p_3][self.position_y_p_3] = self.symbol_p_3
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_p_3][destination_y_p_3] != '.' :
                            if self.board[destination_x_p_3][destination_y_p_3] == self.board[self.position_x_p_3-1][self.position_y_p_3-1]:
                                self.board[self.position_x_p_3][self.position_y_p_3] = '.'
                                self.position_x_p_3 = destination_x_p_3
                                self.position_y_p_3 = destination_y_p_3
                                self.board[self.position_x_p_3][self.position_y_p_3] = self.symbol_p_3
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_p_3][destination_y_p_3] == self.board[self.position_x_p_3-1][self.position_y_p_3+1]:
                                self.board[self.position_x_p_3][self.position_y_p_3] = '.'
                                self.position_x_p_3 = destination_x_p_3
                                self.position_y_p_3 = destination_y_p_3
                                self.board[self.position_x_p_3][self.position_y_p_3] = self.symbol_p_3
                        
                                return self.board
                                break 
                        continue
            except:
                pass

class WHITE_PAWN_4(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_p_4 = 6
        self.position_y_p_4 = 4
        self.symbol_p_4 = 'P'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for white_pawn_4',(self.position_x_p_4,self.position_y_p_4))
                destination_x_p_4 = int(input('row:'))
                destination_y_p_4 = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_p_4][destination_y_p_4] == '.' :

                        if abs(self.position_x_p_4-destination_x_p_4) == 1 and abs(self.position_y_p_4-destination_y_p_4) == 0 :
                            self.board[self.position_x_p_4][self.position_y_p_4] = '.'
                            self.position_x_p_4 = destination_x_p_4
                            self.position_y_p_4 = destination_y_p_4
                            self.board[self.position_x_p_4][self.position_y_p_4] = self.symbol_p_4
                        
                            return self.board
                            break
                        
                        elif (self.position_x_p_4,self.position_y_p_4) == (6,4):
                            if abs(self.position_x_p_4-destination_x_p_4) == 2 and abs(self.position_y_p_4-destination_y_p_4) == 0 :
                                self.board[self.position_x_p_4][self.position_y_p_4] = '.'
                                self.position_x_p_4 = destination_x_p_4
                                self.position_y_p_4 = destination_y_p_4
                                self.board[self.position_x_p_4][self.position_y_p_4] = self.symbol_p_4
                        
                                return self.board
                                break
                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        if self.board[destination_x_p_4][destination_y_p_4] != '.' :
                            
                            if self.board[destination_x_p_4][destination_y_p_4] == self.board[self.position_x_p_4-1][self.position_y_p_4-1]:
                                self.board[self.position_x_p_4][self.position_y_p_4] = '.'
                                self.position_x_p_4 = destination_x_p_4
                                self.position_y_p_4 = destination_y_p_4
                                self.board[self.position_x_p_4][self.position_y_p_4] = self.symbol_p_4
                        
                                return self.board
                                break
                                
                            if self.board[destination_x_p_4][destination_y_p_4] == self.board[self.position_x_p_4-1][self.position_y_p_4+1]:
                                self.board[self.position_x_p_4][self.position_y_p_4] = '.'
                                self.position_x_p_4 = destination_x_p_4
                                self.position_y_p_4 = destination_y_p_4
                                self.board[self.position_x_p_4][self.position_y_p_4] = self.symbol_p_4
                        
                                return self.board
                                break    
                        continue
            except:
                pass

class BLACK_BISHOP_R(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_BB_r = 0
        self.position_y_BB_r = 5
        self.symbol_BB_r = 'B'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for BLACK_BISHOP_R',(self.position_x_BB_r,self.position_y_BB_r))
                destination_x_BB_r = int(input('row:'))
                destination_y_BB_r = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[1][4]  == 'P':
                        print('Cannot move a BLACK_BISHOP_R because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_BB_r][destination_y_BB_r] == '.' :

                            if  abs(self.position_x_BB_r-destination_x_BB_r) == abs(self.position_y_BB_r-destination_y_BB_r) :
                                self.board[self.position_x_BB_r][self.position_y_BB_r] = '.'
                                self.position_x_BB_r = destination_x_BB_r
                                self.position_y_BB_r = destination_y_BB_r
                                self.board[self.position_x_BB_r][self.position_y_BB_r] = self.symbol_BB_r

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass
    
class BLACK_KNIGHT_R(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_BKN_r = 0
        self.position_y_BKN_r = 6
        self.symbol_BKN_r = 'N'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for BLACK_KNIGHT_R',(self.position_x_BKN_r,self.position_y_BKN_r))
                destination_x_BKN_r = int(input('row:'))
                destination_y_BKN_r = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_BKN_r][destination_y_BKN_r] == '.' :

                        if abs(self.position_x_BKN_r-destination_x_BKN_r)**2 + abs(self.position_y_BKN_r-destination_y_BKN_r)**2 == 5 :
                            self.board[self.position_x_BKN_r][self.position_y_BKN_r] = '.'
                            self.position_x_BKN_r = destination_x_BKN_r
                            self.position_y_BKN_r = destination_y_BKN_r
                            self.board[self.position_x_BKN_r][self.position_y_WKN_r] = self.symbol_BKN_r

                            return self.board
                            break

                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        print("your move is invalid,because this part is full")
                        continue
            except:
                pass 



class BLACK_ROOK_R(Chess_Board):

    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_BR_R = 0
        self.position_y_BR_R = 7
        self.symbol_BR_R = 'R'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for BLACK_ROOK_R ',( self.position_x_BR_R,self.position_y_BR_r))
                destination_x_BR_R = int(input('row:'))
                destination_y_BR_R = int(input('column:'))
                
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[1][7]  == 'P':
                        print('Cannot move a BLACK_ROOK_R because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_BR_R][destination_y_BR_R] == '.' :

                            if (destination_x_BR_R == self.position_x_BR_R or destination_y_BR_R==self.position_y_BR_R  ):
                                self.board[self.position_x_WR_R][self.position_y_BR_R] = '.'
                                self.position_x_BR_R = destination_x_BR_R
                                self.position_y_BR_R = destination_y_BR_R
                                self.board[self.position_x_BR_R][self.position_y_BR_R] = self.symbol_BR_R

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass
            
class BLACK_QUEEN(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_BQ = 0
        self.position_y_BQ  = 3
        self.symbol_BQ  = 'Q'
                                                                                                                                                                                                                  
    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for BLACK_QUEEN',( self.position_x_BQ,self.position_y_BQ))
                destination_x_BQ  = int(input('row:'))
                destination_y_BQ  = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[1][3]  == 'P':
                        print('Cannot move a BLACK_QUEEN because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_BQ][destination_y_BQ ] == '.' :

                            if (destination_x_BQ  == self.position_x_BQ  or destination_y_BQ==self.position_y_BQ or abs(self.position_x_BQ-destination_x_BQ) == abs(self.position_y_BQ-destination_y_BQ) ):
                                self.board[self.position_x_BQ][self.position_y_BQ] = '.'
                                self.position_x_BQ = destination_x_BQ
                                self.position_y_BQ = destination_y_BQ
                                self.board[self.position_x_BQ][self.position_y_BQ] = self.symbol_BQ                                                                                                                
                                
                                return self.board
                                break
                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass


class BLACK_BISHOP_L(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_BB = 0
        self.position_y_BB= 2
        self.symbol_BB = 'B'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for BLACK_BISHOP_L',( self.position_x_BB,self.position_y_BB))
                destination_x_BB = int(input('row:'))
                destination_y_BB = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[1][3]  == 'P':
                        print('Cannot move a BLACK_BISHOP_L because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_BB][destination_y_BB] == '.' :

                            if  abs(self.position_x_BB-destination_x_BB) == abs(self.position_y_BB-destination_y_BB) :
                                self.board[self.position_x_BB][self.position_y_BB] = '.'
                                self.position_x_BB = destination_x_BB
                                self.position_y_BB = destination_y_BB
                                self.board[self.position_x_BB][self.position_y_BB] = self.symbol_BB

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass


class BLACK_KNIGHT_L(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_BKN = 0
        self.position_y_BKN = 1
        self.symbol_BKN = 'N'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for BLACK_KNIGHT_L',( self.position_x_BKN,self.position_y_BKN))
                destination_x_BKN = int(input('row:'))
                destination_y_BKN = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_BKN][destination_y_BKN] == '.' :
                         

                        if abs(self.position_x_BKN-destination_x_BKN)**2 + abs(self.position_y_BKN-destination_y_BKN)**2 == 5 :
                            self.board[self.position_x_BKN][self.position_y_BKN] = '.'
                            self.position_x_BKN = destination_x_BKN
                            self.position_y_BKN = destination_y_BKN
                            self.board[self.position_x_BKN][self.position_y_BKN] = self.symbol_BKN

                            return self.board
                            break

                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                            print("your move is invalid,because this part is full")
                            continue
                    
            except:
                pass



class BLACK_ROOK_L(Chess_Board):

    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_BR = 0
        self.position_y_BR = 0
        self.symbol_BR = 'R'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for BLACK_ROOK_L ',( self.position_x_BR,self.position_y_BR))
                destination_x_BR = int(input('row:'))
                destination_y_BR = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:
                    if self.board[1][0]  == 'P':
                        print('Cannot move a BLACK_ROOK_L because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_BR][destination_y_BR] == '.' :

                            if (destination_x_BR == self.position_x_BR or destination_y_BR==self.position_y_BR  ):
                                self.board[self.position_x_BR][self.position_y_BR] = '.'
                                self.position_x_BR = destination_x_BR
                                self.position_y_BR = destination_y_BR
                                self.board[self.position_x_BR][self.position_y_BR] = self.symbol_BR

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass


class BLACK_KING(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_BK = 0
        self.position_y_BK = 4
        self.symbol_BK = 'K'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for BLACK_KING',( self.position_x_BK,self.position_y_BK))
                destination_x_BK = int(input('row:'))
                destination_y_BK = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[1][4]  == 'P':
                        print('Cannot move a BLACK_KING because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_BK][destination_y_BK] == '.' :

                            if ( abs(self.position_x_BK-destination_x_BK) <2 and abs(self.position_y_BK-destination_y_BK) < 2 ):
                                self.board[self.position_x_BK][self.position_y_BK] = '.'
                                self.position_x_BK = destination_x_BK
                                self.position_y_BK = destination_y_BK
                                self.board[self.position_x_BK][self.position_y_BK] = self.symbol_BK

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass




class WHITE_KING(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WK = 7
        self.position_y_WK = 4
        self.symbol_WK = 'K'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE KING',( self.position_x_WK,self.position_y_WK))
                destination_x_WK = int(input('row:'))
                destination_y_WK = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:    
                    if self.board[6][4]  == 'P':
                        print('Cannot move a WHITE_KING because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_WK][destination_y_WK] == '.' :

                            if ( abs(self.position_x_WK-destination_x_WK) <2 and abs(self.position_y_WK-destination_y_WK) < 2 ):
                                self.board[self.position_x_WK][self.position_y_WK] = '.'
                                self.position_x_WK = destination_x_WK
                                self.position_y_WK = destination_y_WK
                                self.board[self.position_x_WK][self.position_y_WK] = self.symbol_WK

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass


class WHITE_QUEEN(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WQ = 7
        self.position_y_WQ = 3
        self.symbol_WQ = 'Q'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE QUEEN',( self.position_x_WQ,self.position_y_WQ))
                destination_x_WQ = int(input('row:'))
                destination_y_WQ = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                else:    
                    if self.board[6][3] == 'P':
                        print('Cannot move a WHITE_QUEEN because it is a pawn in front of it')
                        continue
                        
                    else:
                        if self.board[destination_x_WQ][destination_y_WQ] == '.':

                            if (destination_x_WQ == self.position_x_WQ or destination_y_WQ==self.position_y_WQ or abs(self.position_x_WQ-destination_x_WQ) == abs(self.position_y_WQ-destination_y_WQ) ):
                                self.board[self.position_x_WQ][self.position_y_WQ] = '.'
                                self.position_x_WQ = destination_x_WQ
                                self.position_y_WQ = destination_y_WQ
                                self.board[self.position_x_WQ][self.position_y_WQ] = self.symbol_WQ                                                                                                                 
                                
                                return self.board                                                                                                                                             
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass

class WHITE_ROOK_L(Chess_Board):

    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WR = 7
        self.position_y_WR = 0
        self.symbol_WR = 'R'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE ROOK_L ',( self.position_x_WR,self.position_y_WR))
                destination_x_WR = int(input('row:'))
                destination_y_WR = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[6][0]  == 'P':
                        print('Cannot move a WHITE_ROOK_L because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_WR][destination_y_WR] == '.' :

                            if (destination_x_WR == self.position_x_WR or destination_y_WR==self.position_y_WR  ):
                                self.board[self.position_x_WR][self.position_y_WR] = '.'
                                self.position_x_WR = destination_x_WR
                                self.position_y_WR = destination_y_WR
                                self.board[self.position_x_WR][self.position_y_WR] = self.symbol_WR

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass

class WHITE_BISHOP_L(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WB = 7
        self.position_y_WB = 2
        self.symbol_WB = 'B'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE BISHOP_L',( self.position_x_WB,self.position_y_WB))
                destination_x_WB = int(input('row:'))
                destination_y_WB = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[6][3]  == 'P':
                        print('Cannot move a WHITE_BISHOP_L because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_WB][destination_y_WB] == '.' :

                            if  abs(self.position_x_WB-destination_x_WB) == abs(self.position_y_WB-destination_y_WB) :
                                self.board[self.position_x_WB][self.position_y_WB] = '.'
                                self.position_x_WB = destination_x_WB
                                self.position_y_WB = destination_y_WB
                                self.board[self.position_x_WB][self.position_y_WB] = self.symbol_WB

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass

class WHITE_KNIGHT_L(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WKN = 7
        self.position_y_WKN = 1
        self.symbol_WKN = 'N'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE KNIGHT_L',( self.position_x_WKN,self.position_y_WKN))
                destination_x_WKN = int(input('row:'))
                destination_y_WKN = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_WKN][destination_y_WKN] == '.' :

                        if abs(self.position_x_WKN-destination_x_WKN)**2 + abs(self.position_y_WKN-destination_y_WKN)**2 == 5 :
                            self.board[self.position_x_WKN][self.position_y_WKN] = '.'
                            self.position_x_WKN = destination_x_WKN
                            self.position_y_WKN = destination_y_WKN
                            self.board[self.position_x_WKN][self.position_y_WKN] = self.symbol_WKN

                            return self.board
                            break

                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        print("your move is invalid,because this part is full")
                        continue
            except:
                pass


class WHITE_ROOK_R(Chess_Board):

    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WR_R = 7
        self.position_y_WR_R = 7
        self.symbol_WR_R = 'R'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE ROOK_R ',( self.position_x_WR_R,self.position_y_WR_R))
                destination_x_WR_R = int(input('row:'))
                destination_y_WR_R = int(input('column:'))
                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[6][7]  == 'P':
                        print('Cannot move a WHITE_ROOK_R because it is a pawn in front of it')
                        continue
                    else:
                        if self.board[destination_x_WR_R][destination_y_WR_R] == '.' :

                            if (destination_x_WR_R == self.position_x_WR_R or destination_y_WR_R==self.position_y_WR_R  ):
                                self.board[self.position_x_WR_R][self.position_y_WR_R] = '.'
                                self.position_x_WR_R = destination_x_WR_R
                                self.position_y_WR_R = destination_y_WR_R
                                self.board[self.position_x_WR_R][self.position_y_WR_R] = self.symbol_WR_R

                                return self.board
                                break

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass


class WHITE_KNIGHT_R(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WKN_r = 7
        self.position_y_WKN_r = 6
        self.symbol_WKN_r = 'N'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE KNIGHT_R',( self.position_x_WKN_r,self.position_y_WKN_r))
                destination_x_WKN_r = int(input('row:'))
                destination_y_WKN_r = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                    if self.board[destination_x_WKN_r][destination_y_WKN_r] == '.' :

                        if abs(self.position_x_WKN_r-destination_x_WKN_r)**2 + abs(self.position_y_WKN_r-destination_y_WKN_r)**2 == 5 :
                            self.board[self.position_x_WKN_r][self.position_y_WKN_r] = '.'
                            self.position_x_WKN_r = destination_x_WKN_r
                            self.position_y_WKN_r = destination_y_WKN_r
                            self.board[self.position_x_WKN_r][self.position_y_WKN_r] = self.symbol_WKN_r

                            return self.board
                            break

                        else:
                            print ('your move is invalid, please choose coordinates again')
                            continue
                    else:
                        print("your move is invalid,because this part is full")
                        continue
            except:
                pass            

class WHITE_BISHOP_R(Chess_Board):
    def __init__(self):
        Chess_Board.__init__(self)
        self.position_x_WB_r = 7
        self.position_y_WB_r = 5
        self.symbol_WB_r = 'B'

    def move(self):
        while True:
            try:
                print ('give a x and y coordinate for WHITE BISHOP_R',( self.position_x_WB_r,self.position_y_WB_r))
                destination_x_WB_r = int(input('row:'))
                destination_y_WB_r = int(input('column:'))

                again = input("again:(Y/N)")
                if again == 'Y':
                    return self.board
                    
                else:  
                
                    if self.board[6][4]  == 'P' or self.board[6][6]  == 'P':
                        print('Cannot move a WHITE_BISHOP_R because it is a pawn in front of it')
                        continue
                    
                    else:
                        
                        if self.board[destination_x_WB_r][destination_y_WB_r] == '.' :

                            if  abs(self.position_x_WB_r-destination_x_WB_r) == abs(self.position_y_WB_r-destination_y_WB_r) :
                                self.board[self.position_x_WB_r][self.position_y_WB_r] = '.'
                                self.position_x_WB_r = destination_x_WB_r
                                self.position_y_WB_r = destination_y_WB_r
                                self.board[self.position_x_WB_r][self.position_y_WB_r] = self.symbol_WB_r

                                return self.board
                                

                            else:
                                print ('your move is invalid, please choose coordinates again')
                                continue
                        else:
                            print("your move is invalid,because this part is full")
                            continue
            except:
                pass

class Engine(Chess_Board):

    def __init__(self):
        WHITE_PAWN_0.__init__(self)
        WHITE_PAWN_1.__init__(self)
        WHITE_PAWN_2.__init__(self)
        WHITE_PAWN_3.__init__(self)
        WHITE_PAWN_4.__init__(self)
        WHITE_PAWN_5.__init__(self)
        WHITE_PAWN_6.__init__(self)
        WHITE_PAWN_7.__init__(self)
        BLACK_PAWN_7.__init__(self)
        BLACK_PAWN_6.__init__(self)
        BLACK_PAWN_5.__init__(self)
        BLACK_PAWN_4.__init__(self)
        BLACK_PAWN_3.__init__(self)
        BLACK_PAWN_2.__init__(self)
        BLACK_PAWN_1.__init__(self)
        BLACK_PAWN_0.__init__(self)
        WHITE_KING.__init__(self)
        WHITE_QUEEN.__init__(self)
        WHITE_ROOK_L.__init__(self)
        WHITE_BISHOP_L.__init__(self)
        WHITE_BISHOP_R.__init__(self)
        WHITE_KNIGHT_L.__init__(self)
        WHITE_KNIGHT_R.__init__(self)
        WHITE_ROOK_R.__init__(self)
        BLACK_KING.__init__(self)
        BLACK_ROOK_L.__init__(self)
        BLACK_KNIGHT_L.__init__(self)
        BLACK_BISHOP_L.__init__(self)
        BLACK_QUEEN.__init__(self)
        BLACK_ROOK_R.__init__(self)
        BLACK_KNIGHT_R.__init__(self)
        BLACK_BISHOP_R.__init__(self)
        Chess_Board.__init__(self)
    
    def play(self):
        
        #print('PLEASE WRITE WHAT FIGURE YOU CHOOSE TO MOVE: white_king, white_queen, white_rook_L, white_bishop_L'
              #',white_knight_L, white_rook_R, white_knight_R, white_bishop_R, black_king,black_rook_L,black_knight_L'
              #',black_bishop_L,black_queen,black_rook_R,black_knight_R,black_bishop_R,white_pawn_4,white_pawn_3,white_pawn_2'
              #',white_pawn_1,white_pawn_0,white_pawn_5,white_pawn_6,white_pawn_7,black_pawn_4,black_pawn_3,black_pawn_2'
              # 'black_pawn_1,black_pawn_0,black_pawn_5,black_pawn_6,black_pawn_7')

        while True:
            a = "white"
            b = "black"
            choice=str(input())

            A= [a,b,a,b,a,b,a,b]
            print(A)
            for i in range(len(A)):
                i += 1
                if i == b:
                
                    if  choice == 'black_pawn_0':
                        BLACK_PAWN_0.move(self)
                        break
                    elif  choice == 'black_pawn_1':
                        BLACK_PAWN_1.move(self)
                        break
                    elif  choice == 'black_pawn_2':
                        BLACK_PAWN_2.move(self)
                        break
                    elif  choice == 'black_pawn_3':
                        BLACK_PAWN_3.move(self)
                        break
                    elif  choice == 'black_pawn_4':
                        BLACK_PAWN_4.move(self)
                        break
                    elif  choice == 'black_pawn_5':
                        BLACK_PAWN_5.move(self)
                        break
                    elif  choice == 'black_pawn_6':
                        BLACK_PAWN_6.move(self)
                        break
                    elif  choice == 'black_pawn_7':
                        BLACK_PAWN_7.move(self)
                        break
                    elif  choice == 'black_rook_L':
                        BLACK_ROOK_L.move(self)
                        break
                    elif  choice == 'black_knight_L':
                        BLACK_KNIGHT_L.move(self)
                        break
                    elif  choice == 'black_bishop_L':
                        BLACK_BISHOP_L.move(self)
                        break
                    elif  choice == 'black_queen':
                        BLACK_QUEEN.move(self)
                        break
                    elif  choice == 'black_rook_R':
                        BLACK_ROOK_R.move(self)
                        break
                    elif  choice == 'black_knight_R':
                        BLACK_KNIGHT_R.move(self)
                        break
                    elif choice == 'black_bishop_R':
                        BLACK_BISHOP_R.move(self)
                        break
                    elif  choice == 'black_king':
                        BLACK_KING.move(self)
                        break
                elif i== a :   
                    if  choice == 'white_pawn_1':
                        WHITE_PAWN_1.move(self)
                        break
                    elif  choice == 'white_pawn_7':
                        WHITE_PAWN_7.move(self)
                        break
                    elif  choice == 'white_pawn_6':
                        WHITE_PAWN_6.move(self)
                        break
                    elif  choice == 'white_pawn_5':
                        WHITE_PAWN_5.move(self)
                        break
                    elif  choice == 'white_pawn_0':
                        WHITE_PAWN_0.move(self)
                        break
                    elif  choice == 'white_pawn_4':
                        WHITE_PAWN_4.move(self)
                        break
                    elif  choice == 'white_pawn_3':
                        WHITE_PAWN_3.move(self)
                        break
                    elif  choice == 'white_pawn_2':
                        WHITE_PAWN_2.move(self)
                        break
                    elif  choice == 'white_bishop_L':
                        WHITE_BISHOP_L.move(self)
                        break
                    elif  choice == 'white_bishop_R':
                        WHITE_BISHOP_R.move(self)
                        break
                    elif  choice == 'white_knight_L':
                        WHITE_KNIGHT_L.move(self)
                        break
                    elif  choice == 'white_knight_R':
                        WHITE_KNIGHT_R.move(self)
                        break
                    elif  choice == 'white_rook_L':
                        WHITE_ROOK_L.move(self)
                        break
                    elif  choice == 'white_rook_R':
                        WHITE_ROOK_R.move(self)
                        break
                    elif  choice == 'white_king':
                        WHITE_KING.move(self)
                        break
                    elif  choice == 'white_queen':
                        WHITE_QUEEN.move(self)
                        break
                else:
                    print ('please choose again')
               

    def display(self):
        for i in range (8):
            for j in range (8):
                print (self.board[i][j], end=' ')
            print ()
            

c_engine = Engine()
c_engine.display()
while True:
    c_engine.play()
    c_engine.display()
    
