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
