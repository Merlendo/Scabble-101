def board():
    board=[]
    for i in range (15):
        line=[]
        for j in range(15):
            line.append("x")
        board.append(line)
    return board

def affichageBoard(board):
    
    for line in board:
        for elem in line:
            print(elem, end=" ")
        print()

b = board() 
affichageBoard(b)
#print(board())

def changeBoard(lettre, position, board):
    board[position[0]-1].pop(position[1]-1)
    board[position[0]-1].insert(position[1]-1,lettre)
    return board

#POSITION = (ligne,col)
position = (15,6)
b = changeBoard("a", position, b)
print()
affichageBoard(b)
