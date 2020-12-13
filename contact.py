from plateau import board, init_bonus, affichageBoard
from construction_mots import mot_jouable, generer_dico, mots_jouables
from placement import tester_placement, placer_mot
import os




def contact(board,mot,direction,ligne,colonne,dico):
    vide=[" ","MT","MD","LT","LD"]
    verif=True

    if direction == "horizontale":

        while verif and colonne<len(mot):
            for elem in mot :
                temp_liste=[]
                liste=[]
                mot_temp=[]
                
                if board[ligne-1][colonne] not in vide or board[ligne+1][colonne] not in vide:

                ##PARCOURS LES CARACTERES AU DESSUS
                    l=ligne-1
                    while board[l][colonne] not in vide:
                        temp_liste.append(board[l][colonne])
                        l=l-1
                        print("l: ",l)
                    ## REMETTRE LETTRES DANS L'ORDRE
                    for i in range (len(temp_liste)):
                        liste.append(temp_liste[-i-1])

                ##AJOUTE LA LETTRE DU MOT 
                    liste.append(elem)

                ##PARCOURS LES CARACTERES EN DESSOUS
                    l=ligne+1
                    while board[l][colonne] not in vide:
                        liste.append(board[l][colonne])
                        l=l+1
                    
                    ##VERIF EXISTENCE DES MOTS
                    mot_temp="".join(liste)

                    if mot_temp not in dico and liste!=[elem]:
                        verif=False
                    else:
                        verif=True
                else:
                    verif=True
                
                colonne=colonne+1
    

    if direction == "verticale":
        print("direction: verticale")

        while verif and ligne<len(mot):
            print("verif: ",verif)
            for elem in mot :
                print("elem: ",elem)
                temp_liste=[]
                liste=[]
                mot_temp=[]
                
                
                print("colonne-1: ",colonne-1)
                print("board[ligne][colonne-1]: ",board[ligne][colonne-1])

                if board[ligne][colonne-1] not in vide or board[ligne][colonne+1] not in vide:
                    print("non vide")
                    print("condition booléenne: ",board[ligne][colonne-1],"pour ",elem)

                ##PARCOURS LES CARACTERES AU DESSUS
                    c=colonne-1
                    while board[ligne][c] not in vide:
                        temp_liste.append(board[ligne][c])
                        c=c-1
                        print("c: ",c)
                    ## REMETTRE LETTRES DANS L'ORDRE
                    for i in range (len(temp_liste)):
                        liste.append(temp_liste[-i-1])

                ##AJOUTE LA LETTRE DU MOT 
                    liste.append(elem)

                ##PARCOURS LES CARACTERES EN DESSOUS
                    c=colonne+1
                    while board[ligne][c] not in vide:
                        liste.append(board[ligne][c])
                        c=c+1
                    
                    ##VERIF EXISTENCE DES MOTS
                    mot_temp="".join(liste)
                    a=[elem]
                    print("verificateur: ",liste==[])
                    if not(mot_temp  in dico or liste==a):
                        verif=False
                    else:
                        verif=True
                else:
                    verif=True
                
                ligne=ligne+1

    return verif
