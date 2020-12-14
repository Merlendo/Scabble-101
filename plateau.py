import copy

#Créer un plateau de 15*15
def board():
    board=[]
    for i in range(15):
        line=[]
        for j in range(15):
            line.append(" ")
        board.append(line)
    return board

#Formate l'affichage du plateau pour le rendre plus esthétique, ne le modifie pas
def affichageBoard(board):
    affBoard = copy.deepcopy(board)
    coord = [" "," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
    vide = ["_"*50]
    affBoard.insert(0,coord)
    affBoard.insert(1,vide)

    for i in range(2,len(affBoard)):
        affBoard[i].insert(0,str(i-1))
        affBoard[i].insert(1,'|')
 
    for line in affBoard:
        for elem in line:
            print(elem.rjust(2), end=" ")
        print()

#Permet de placer une lettre sur une case du plateau
def changeBoard(lettre, position, board):
    board[position[0]].pop(position[1])
    board[position[0]].insert(position[1],lettre)
    return board

#Place les bonus sur le plateau
def init_bonus(board):
    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

    for position in cases_MT:
        changeBoard('*', position, board) #mot triple
    for position in cases_MD:
        changeBoard("^", position, board) #mot double
    for position in cases_LT:
        changeBoard("-", position, board) #lettre triple
    for position in cases_LD:
        changeBoard("+", position, board) #lettre double
