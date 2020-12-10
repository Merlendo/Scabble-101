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



def lire_coords():

    i = int(input("donner la ligne ou vous voulez placer le jetons "))
    while i<0 or i>14 :
        i = int(input("donner la ligne ou vous voulez placer le jetons "))
    j = int(input("donner la colone ou vous voulez placer le jetons "))
    while j<0 or j>14 :
        j = int(input("donner la colone ou vous voulez placer le jetons "))

    return i,j

def tester_placement(plateau,i,j,direction,mot):

    ok = True
    l = []

    if direction.lower() == "horizontale":

        if len(mot) >= 15 - j:
            ok = False
            print("longueur")
        else :
            for x in range(j,len(mot)):
                if plateau [i][x]!= mot[x-j] or plateau[i][x] not in ["x","MT","MD","LT","LD"]:
                    ok = False
                    print("error: ",plateau[i][x])
        print("ok: ",ok)
        if ok :  
            x = j
            for e in mot :
                print(plateau[i][x])
                if plateau[i][x] in ["x","MT","MD","LT","LD"] :
                    l.append(e)
                x = x+1
                    
    if direction.lower() == "verticale":

        if len(mot) >= 15 - i:
            ok = False
        else :
            for x in range(i,len(mot)):
                if plateau [x][j]!= mot[x-i] or plateau[i][x] not in ["x","MT","MD","LT","LD"]:
                    ok = False

        if ok :  
            x = i
            for e in mot :
                print(plateau[x][j])
                if plateau[x][j] in ["x","MT","MD","LT","LD"] :
                    l.append(e)
                x = x+1
    return l

def placer_mot(plateau,lm,mot,i,j,dr):
    
    l = tester_placement(plateau,i,j,dr,mot)
    print("l= ",l)
    
    
    if len(l)!= 0 :
        
        if direction.lower() == "horizontale":
            x = j
            for e in mot :
                if e in l :
                    plateau[i][x] = e
                    lm.remove(e)
                x = x + 1
        if direction.lower() == "verticale":
            x = i
            for e in mot :
                if e in l :
                    plateau[x][j] = e
                    lm.remove(e)
                x = x + 1
        ok = True
    else :
        ok = False
        
    return ok


##b[7][7]="T"
##b[7][14]="S"

hand=['t','h','e','i','e','r','e','s']
mot=input('mot: ')
x,y=lire_coords()
direction=input('horizontale/verticale: ')

print("board: ",b)
print("tester_placement: ",tester_placement(b,x,y,direction,mot))
print("hand: ",hand)

print("placer_mot: ",placer_mot(b,hand,mot,x,y,direction))
print("hand= ",hand)
print(b[4])
print(b)
affichageBoard(b)
