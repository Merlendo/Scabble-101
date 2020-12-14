from plateau import board, init_bonus, affichageBoard
import os

def coords_check(coords):
    temp = [c for c in coords]
    newcoords = []
    if (temp[0] in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]) and (int(temp[1]) in [x for x in range(16) if x > 0]):
        newcoords.append((ord(temp[0]) - ord("A"))%26+1) 
        newcoords.append(int(temp[1]))
        return newcoords
    else:
        return False


def lire_coords():
    verification = True
    while verification:
        os.system('cls')
        print("Quelles coordonnées ? (ex : A5)")
        coords = input("> ")
        if coords_check(coords) != False:
            coords = coords_check(coords)
            verification = False
    
    direction = ""
    POSSIBILITE = ["horizontale","verticale"]
    while direction.lower() not in POSSIBILITE:
        os.system('cls')
        print("Dans quelle direction ? (horizontale/verticale)")
        direction = input("> ")
        
    return coords, direction.lower()



def tester_placement(board,i,j,direction,mot):
    vide=[" ","MT","MD","LT","LD"]
    drapeau = True
    lettres_necessaires = []

    if direction=="horizontale":
        if len(mot) > 15 - j:
            drapeau = False
            print("mot trop long")
        else:
            for colonne in range (j,j+len(mot)):
                if not (board[i][colonne] in vide or board[i][colonne] != mot[colonne-j]):
                    drapeau=False
                    print("erreur",board[i][colonne])
        if drapeau:
            colonne=j
            for elem in mot :
                if board[i][colonne] in vide:
                    lettres_necessaires.append(elem)
                colonne=colonne+1
    

    if direction == "verticale":
        if len(mot) > 15 - i:
            drapeau = False
            print("mot trop long")
        else :
            for ligne in range(i,i+len(mot)):
                if not (board[ligne][j] in vide or board[ligne][j] != mot[ligne-i]):
                    drapeau = False
                    print("erreur",board[j][ligne])

        if drapeau :  
            ligne = i
            for elem in mot :
                if board[ligne][j] in vide :
                    lettres_necessaires.append(elem)
                ligne = ligne+1

    return lettres_necessaires

def placer_mot(board,main,mot,i,j,direction):

    lettres_necessaires=tester_placement(board,i,j,direction,mot)
    if len(lettres_necessaires)!=0:
        if direction == "horizontale":

            colonne=j
            for elem in mot:
                if elem in lettres_necessaires:
                    board[i][colonne]=elem.upper()
                    main.remove(elem)
                colonne=colonne+1
        
        if direction == "verticale":
            ligne = i
            for elem in mot :
                if elem in lettres_necessaires :
                    board[ligne][j] = elem.upper()
                    main.remove(elem)
                ligne = ligne + 1
        drapeau=True
    
    else:
        drapeau=False
    return drapeau

def comptage(board,mot,direction,i,j):
    vide=["x","MT","MD","LT","LD"]
    bonus_lettres=["LT","LD"]
    bonus_mot=["MT","MD"]
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

    if direction == "verticale":
        ligne=i

        for elem in mot:

            if board[ligne][j] in bonus_lettres:

                if board[ligne][j] == "LT":
                    valeurs_bonus_lettres.append(3)
                else:
                    valeurs_bonus_lettres.append(2)

            elif board[ligne][j] in bonus_mot:
                valeurs_bonus_lettres.append(1)

                if board[ligne][j]=="MT":
                    valeurs_bonus_mot[0]=3
                else:
                    valeurs_bonus_mot[1]=2

            else:
                valeurs_bonus_lettres.append(1)

            ligne=ligne+1

    values=[valeurs_bonus_mot,valeurs_bonus_lettres]

    return values   

"""b = board()
init_bonus(b)
possible = tester_placement(b,5,3,'verticale','robinet')
print(possible)
placer_mot(b,["r","o","b","i","n","e","t"],'robinet',5,3,'verticale')
#print(b)

affichageBoard(b)"""
