cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

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

def changeBoard(lettre, position, board):
    board[position[0]].pop(position[1])
    board[position[0]].insert(position[1],lettre)
    return board

def init_bonus(board):
    for position in cases_MT:
        changeBoard('MT', position, board)
    for position in cases_MD:
        changeBoard("MD", position, board)
    for position in cases_LT:
        changeBoard("LT", position, board)
    for position in cases_LD:
        changeBoard("LD", position, board)

#COMPARE LE PLATEAU AVANT L'APPLICATION DES BONUS ET APRES
b = board()
affichageBoard(b)
print()
init_bonus(b)
affichageBoard(b)


def lire_coords(board):
    x=int(input("colonne: "))
    y=int(input("ligne: "))
    while x>15 or y>15:
        x=int(input("colonne: "))
        y=int(input("ligne: "))
        print(board[y][x])
    return x, y

def tester_placement(board,x,y,direction,mot):
    initialisation = board[y][x] 
    lettres=list(mot.upper())
    print("liste lettres du mot: ",lettres)
    liste_lettres=[]
    lettres_necessaires=[]
    
    if str(direction.upper()) == "HORIZONTALE" and len(mot)<=15-x:
        for i in range (len(mot)):
            ##print("i: ",i)
            ##print("board: ",board[y][i+x])

            if board[y][i+x] not in ["x","MT","MD","LT","LD"]:
                liste_lettres.append(board[y][i+x])
        ##if liste_lettres in lettres or liste_lettres == ["s"]:
          ##  lettres_necessaires=lettres-liste_lettres
            ##print("liste_lettres: ",liste_lettres)
        if liste_lettres != []:
            for l in liste_lettres:
                ##print("l=",l)
                lettres.remove(l)

    elif direction.upper() == "VERTICALE" and len(mot)<=15-y:
        for i in range (len(mot)):
            if board[i+y][x] not in 'xMTMDLTLD':
                liste_lettres.append(board[i+y][x])
        ##if liste_lettres in lettres or liste_lettres == ["s"]:
          ##  lettres_necessaires=lettres-liste_lettres
        if liste_lettres != []:
            for l in liste_lettres:
                ##print("l=",l)
                lettres.remove(l)
    else:
        lettres=[-1]
    
    return lettres,liste_lettres

##def placer_mot(board,main,mot,x,y,direction):
  ##  lettres_necessaires=tester_placement(board,x,y,direction,mot)
    ##possible=False
    ##if lettres_necessaires in main:
##        possible=True
  ##      if direction.lower()=="horizontale":
    ##        for k in len(mot):
      ##          for i in lettres_necessaires:
        ##            if i in main : 
          ##              main.pop(i)
            ##        board[y][x+k]=i
##        if direction.lower()=="horizontale":
  ##          for k in len(mot):
    ##            for i in lettres_necessaires:
      ##              if i in main : 
        ##                main.pop(i)
          ##          board[y+k][x]=i
    ##return possible

hand=['t','h','e','i','e','r','e']
i=0
##while i <2:
mot=input('mot: ')
x,y=lire_coords(b)
direction=input('horizontale/verticale: ')
    ##placer_mot(b,hand,mot,x,y,direction)
    
b[7][7]="T"
b[7][10]="S"
print(b)
print(hand)
a,m=tester_placement(b,x,y,direction,mot)
print(a)
print(m)
    ##i=i+1
