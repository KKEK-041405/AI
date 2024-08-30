board = [0,2,2,2,2,2,2,2,2,2]

def make2():
    if board[5] == 2: return 5
    #check for non corner elements
    for i in [2,4,6,8]:
        if board[i] == 2: return i

def go(n,player):
    if player == 5:
        print("AI decided to place at pos: ",n)
    else:
        print("you decided to place mark at: ",n)
    board[n] = player

def possWin(player):
    traget = 0
    if player == 5:
        traget = 50
    else:
        traget = 18
    
    #horizontal check
    for i in range(3):
        product = 1
        for j in range(3):
            product *= board[(i*3) + j +1]
        if product == traget:
            for j in range(3):
                if board[(i*3) + j +1] == 2: return (i*3) + j +1
    
    #vertical check
    for i in range(3):
        product = 1
        for j in range(3):
            product *= board[(j*3) + i +1]
        if product == traget:
            for j in range(3):
                if board[(j*3) + i +1] == 2: return (j*3) + i +1
    #diagonal check
    if board[1] * board[5] * board[9] == traget:
        if board[1] == 2:return 1
        if board[5] == 2:return 5
        if board[9] == 2:return 9
    if board[3] * board[5] * board[7] == traget:
        if board[3] == 2:return 3
        if board[5] == 2:return 5
        if board[7] == 2:return 7
    return 0

def Computer(i,mark):
    if i == 1: go(5,mark)
    if i == 2:
        if board[5] == 2:
            go(5,mark)
        else:
            go(1,mark)
    if i == 3:
        if board[9] == 2:
            go(9,mark)
        else:
            go(3,mark)
    if i == 4:
        if(not possWin(15/mark) == 0): go(possWin(15/mark),mark)
        else: go(make2(),mark)
    if i == 5:
        if(not possWin(mark) == 0): go(possWin(mark),mark)#winning move
        elif(not possWin(15/mark) == 0): go(possWin(15/mark),mark)#block opponet
        elif(board[7] == 2): go(7,mark)
        else:go(3,mark)
    if i == 6 or i == 7 or i == 8 or i == 9:
        if(not possWin(mark) == 0): go(possWin(mark),mark)#winning move
        elif(not possWin(15/mark) == 0): go(possWin(15/mark),mark)#block opponet
        else: go(make2(),mark)

def printBoard():
    for i in range(3):
        for j in range(3):
            if board[(i*3) + j +1] == 3:
                print("O",end="|")
            elif board[(i*3) + j +1] == 5:
                print("X",end="|")
            else:
                print(" ",end="|")
        print("")

def checkWin(player):
    traget = 0
    if player == 5:
        traget = 125
    else:
        traget = 27
    
    #horizontal check
    for i in range(3):
        product = 1
        for j in range(3):
            product *= board[(i*3) + j +1]
        if product == traget:
            return True    
    #vertical check
    for i in range(3):
        product = 1
        for j in range(3):
            product *= board[(j*3) + i +1]
        if product == traget:
            return True
    #diagonal check
    if board[1] * board[5] * board[9] == traget:
        return True
    if board[3] * board[5] * board[7] == traget:
        return True
    return False
def Game():
    print()
    c =  int(input("enter 1 to play frist or enter 0 to play second: "))
    printBoard()
    for i in range(1,10):
        if (i%2) ==  0:
            Computer(i,5)
            printBoard()
            if checkWin(5):
                print("computer won")
                return
        else:
            pos = int(input("where you want to place the mark: "))
            while(board[pos] != 2):
                printBoard()
                pos = int(input("enter a valid pos: "))
            go(pos,3)
            printBoard()
            if checkWin(3):
                print("human won")
                return
    print("It is a TIE!")
Game()
