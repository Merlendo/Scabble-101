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
            print(elem.rjust(2), end=" ")
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


lettres = {'A': {'occ': 9, 'val': 1},
               'B': {'occ': 2, 'val': 3}, 
               'C': {'occ': 2, 'val': 3}, 
               'D': {'occ': 3, 'val': 2}, 
               'E': {'occ': 15, 'val': 1}, 
               'F': {'occ': 2, 'val': 4}, 
               'G': {'occ': 2, 'val': 2}, 
               'H': {'occ': 2, 'val': 4}, 
               'I': {'occ': 8, 'val': 1}, 
               'J': {'occ': 1, 'val': 8}, 
               'K': {'occ': 1, 'val': 10}, 
               'L': {'occ': 5, 'val': 1}, 
               'M': {'occ': 3, 'val': 2}, 
               'N': {'occ': 6, 'val': 1}, 
               'O': {'occ': 6, 'val': 1}, 
               'P': {'occ': 2, 'val': 3}, 
               'Q': {'occ': 1, 'val': 8}, 
               'R': {'occ': 6, 'val': 1}, 
               'S': {'occ': 6, 'val': 1}, 
               'T': {'occ': 6, 'val': 1}, 
               'U': {'occ': 6, 'val': 1}, 
               'V': {'occ': 2, 'val': 4}, 
               'W': {'occ': 1, 'val': 10}, 
               'X': {'occ': 1, 'val': 10}, 
               'Y': {'occ': 1, 'val': 10}, 
               'Z': {'occ': 1, 'val': 10}, 
               '?': {'occ': 2, 'val': 0}}






vide=["x","MT","MD","LT","LD"]
bonus_lettres=["LT","LD"]
bonus_mot=["MT","MD"]
def lire_coor():

    i=int(input("saisir ligne debut du mot"))
    while i<0 or i>15:
        i=int(input("saisir ligne debut du mot"))
    
    j=int(input("saisir colonne debut du mot"))
    while j<0 or j>15:
        j=int(input("saisir colonne debut du mot"))

    return i,j

def tester_placement(board,i,j,direction,mot):

    drapeau = True
    lettres_necessaires = []

    if direction=="horizontale":
        if len(mot) > 15 - j:
            drapeau = False
            print("mot trop long")
        else:
            for colonne in range (j,j+len(mot)):
                if not (board[i][colonne] in vide or board[i][colonne]!=mot[colonne-j]):
                    drapeau=False
                    print("erreur",board[i][colonne])
        if drapeau:

                colonne=j
                for elem in mot :
                    if board[i][colonne] in vide:
                        lettres_necessaires.append(elem)
                    colonne=colonne+1
    
    if direction=="verticale":
        if len(mot) > 15 - i:
            drapeau = False
            print("mot trop long")
        else:
            for ligne in range (i,i+len(mot)):
                if not (board[ligne][j] in vide or board[ligne][j]!=mot[ligne-i]):
                    drapeau=False
                    print("erreur",board[ligne][j])
        if drapeau:

                ligne=i
                for elem in mot :
                    if board[ligne][j] in vide:
                        lettres_necessaires.append(elem)
                    ligne=ligne+1
    
    return lettres_necessaires

def placer_mot(board,main,mot,i,j,direction):

    lettres_necessaires=tester_placement(board,i,j,direction,mot)
    if len(lettres_necessaires)!=0:

        if direction == "horizontale":

            colonne=j
            for elem in mot:
                if elem in lettres_necessaires:
                    board[i][colonne]=elem
                    main.remove(elem)
                colonne=colonne+1
        drapeau=True

        if direction == "verticale":

            ligne=i
            for elem in mot:
                if elem in lettres_necessaires:
                    board[ligne][j]=elem
                    main.remove(elem)
                ligne=ligne+1
        drapeau=True
    
    else:
        drapeau=False
    return drapeau

def comptage(board,mot,direction,i,j):

    valeurs_bonus_mot=[0,0]
    valeurs_bonus_lettres=[]

    if direction == "horizontale":
        colonne=j

        for elem in mot:

            if board[i][colonne] in bonus_lettres:

                if board[i][colonne] == "LT":
                    valeurs_bonus_lettres.append(3)
                else:
                    valeurs_bonus_lettres.append(2)

            elif board[i][colonne] in bonus_mot:
                valeurs_bonus_lettres.append(1)

                if board[i][colonne]=="MT":
                    valeurs_bonus_mot[0]=3
                else:
                    valeurs_bonus_mot[1]=2

            else:
                valeurs_bonus_lettres.append(1)

            colonne=colonne+1

    values=[valeurs_bonus_mot,valeurs_bonus_lettres]

    return values   



def valeur_mot(mot,dico,values_bonus):
    valeur=0
    i=0
    for c in mot.upper():

        valeur=valeur + dico[c]["val"]*values_bonus[1][i]
        i=i+1
    if values_bonus[0][0]!=0:
        valeur=valeur*values_bonus[0][0]
    elif values_bonus[0][1]!=0:
        valeur=valeur*values_bonus[0][1]
    
    return valeur

values=comptage(b,'robinet','horizontale',1,1)

print(tester_placement(b,1,1,'horizontale','robinet'))
print(placer_mot(b,["r","o","b","i","n","e","t"],'robinet',1,1,'horizontale'))

affichageBoard(b)
print()
print("values: ",values)
print("marquer",valeur_mot('robinet',lettres,values),"points")
