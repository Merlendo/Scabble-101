from plateau import board
import os
import time

#Fontion qui prend en paramètre un strig de type 'A5' et le transforme en integer correspondant aux coordonnées du plateau
def coords_check(coords):
    newcoords = []
    if (len(coords) <= 3 and len(coords) > 1 ) and (coords[0] in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]) and (coords[1:] in [str(x) for x in range(16) if x > 0]) :
        newcoords.append((ord(coords[0]) - ord("A"))%26+1) 
        newcoords.append(int(coords[1:]))
        return newcoords
    else:
        return False

#Test si le placement est possible est renvoi les lettres necessaires au plament du mot
def tester_placement(board,i,j,direction,mot):
    vide=[" ","*","^","-","+"]
    drapeau = True
    lettres_necessaires = []

    if direction=="horizontale":
        if len(mot) > 15 - j:
            drapeau = False
            print("mot trop long horizontale ")
            time.sleep(5)
        else:
            for colonne in range (j,j+len(mot)):
                if not (board[i][colonne] in vide or board[i][colonne] == mot[colonne-j]):
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
            print("mot trop long verticale")
            time.sleep(5)
        else :
            for ligne in range(i,i+len(mot)):
                if not (board[ligne][j] in vide or board[ligne][j] == mot[ligne-i]):
                    drapeau = False
                    print("erreur",board[j][ligne])

        if drapeau :  
            ligne = i
            for elem in mot :
                if board[ligne][j] in vide :
                    lettres_necessaires.append(elem)
                ligne = ligne+1

    return lettres_necessaires

#Place le mot
def placer_mot(board,main,mot,i,j,direction,lettres_necessaires):
        if direction == "horizontale":

            colonne=j
            for elem in mot:
                if elem in lettres_necessaires:
                    board[i][colonne]=elem
                    main.remove(elem)
                colonne=colonne+1
        
        if direction == "verticale":
            ligne = i
            for elem in mot :
                if elem in lettres_necessaires :
                    board[ligne][j] = elem
                    main.remove(elem)
                ligne = ligne + 1
        drapeau=True


#Compte les bonus à appliquer au mot placer
def comptage(board,mot,direction,i,j):
    vide=[" ","*","^","-","+"]
    bonus_lettres=["-","+"]
    bonus_mot=["*","^"]
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
