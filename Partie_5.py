vide=["x","MT","MD","LT","LD"]
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
    
    else:
        drapeau=False
    return drapeau

print(tester_placement(b,5,3,'horizontale','robinet'))
print(placer_mot(b,["r","o","b","i","n","e","t"],'robinet',5,3,'horizontale'))
print(b)
