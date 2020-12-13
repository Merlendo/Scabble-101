from pioche import piocher, init_dico, init_pioche, echanger, completer_main
from plateau import affichageBoard, init_bonus, board
from placement import lire_coords, tester_placement, placer_mot, coords_check
from construction_mots import mot_jouable, generer_dico, mots_jouables
import os
import time

def clear_screen():
    os.system('cls')

def initialisation(sac): 
    setup = dict()
    nombreDeJoueurs = int(input("Combien de joueur voulez-vous? : "))
    clear_screen()
    for i in range(nombreDeJoueurs):
        print("Nom du joueur",i+1,":")
        j = input("> ")
        setup[i] = {'main': piocher(7,sac), 'score': 0, 'nom': j}
        clear_screen()
    return setup

def fin_partie(sac, joueurs):
    if len(sac) == 0:
        print("La partie est fini")
        for i in range(len(joueurs)):
            print(joueurs[i]["nom"], ':',joueurs[i]["score"])
        print("Le gagnant est ...")
        #menu()

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

    values=[valeurs_bonus_mot,valeurs_bonus_lettres]

    return values   


def prochain_tour(board, ordre, joueurs, sac, liste_mots, premiertour):
    ordre = (ordre+1)%len(joueurs)
    tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre, liste_mots, premiertour)

def affichage_ecran(board,joueurs,ordre,sac):
    clear_screen()
    affichageBoard(board)
    print("NOM DU JOUEUR :", joueurs[ordre]["nom"])
    #print(["A","Z","E","V","C","?","U"])

    for i in range(len(joueurs)):
        print(joueurs[i]['nom'],joueurs[i]['score'], end='')
    print()
    print(joueurs[ordre]["main"])
    print("TAILLE SAC :", len(sac))

def tour_joueur(board, main, sac, joueurs, ordre, liste_mots, premiertour):
    fin_partie(sac, joueurs)
    #AFFICHAGE DU PLATEAU / ESTHETIQUE / MISE EN PLACE
    affichage_ecran(board,joueurs,ordre,sac)
    #AFFICHER LA TAILLE DU SAC EN PERMANENCE
    #-------------------------------------------------------#

    #ACTION DU TOURS
    action = 0
    POSSIBILITE = ["1", "2", "3"]
    while action not in POSSIBILITE:
        affichage_ecran(board,joueurs,ordre,sac)
        print("1 - PASSER | 2 - ECHANGER | 3 - PLACER")
        action = input("> ")
        

    


    #PASSE LE TOUR - OK
    if action == "1":
        prochain_tour(board, ordre, joueurs, sac,liste_mots,premiertour)

    #ECHANGE DES JETONS - OK
    elif action == "2":
        jetons = []
        selection = ""
        while selection != "fin":
            affichage_ecran(board,joueurs,ordre,sac)
            print(jetons)
            
            print("Quelles jeton échanger ? ('fin' pour arrêter) :")
            selection = input("> ")
            if selection.strip().upper() in main:
                jetons.append(selection.strip().upper())
                main.remove(selection.strip().upper())
            
        
        echanger(jetons,main, sac)

        prochain_tour(board, ordre, joueurs, sac,liste_mots,premiertour)
    
    #PLACE DES JETONS - TESTER LES FONCTION DU MODULES PLACEMENT
    elif action == "3":

        #main = ["A","Z","E","V","C","?","U"]
        verification = True
        #REPARER VERIFICATION
        while verification:
            affichage_ecran(board,joueurs,ordre,sac)
            motsJouable = mots_jouables(liste_mots,main)
            print(motsJouable[:5])

            print("Quelle mot voulez vous placer ?")
            mot = input("> ")
            if mot.upper() in motsJouable or mot == "":
                verification = False
            
            #REMPLACE ? AVEC LETTRE MANQUANTE
            templist = list(mot)
            if '?' in main:
                for i in range(len(templist)):
                    if templist[i].upper() not in main:
                        templist.pop(i)
                        templist.insert(i,'?')
            mot = ''.join(templist).upper()
                        

        #  TESTER LE MOT AVEC LES FONCTIONS CONSTRUCTION_MOTS!!!
    
        verification = True
        while verification:

            affichage_ecran(board,joueurs,ordre,sac)
            print("Quelles coordonnées ? (ex : A5)")
            coords = input("> ")
            
            if coords_check(coords.upper()) != False:
        
                coords = coords_check(coords.upper())
                if not premiertour or ((coords[0] == 8 and coords[1] + len(mot) >= 8) or (coords[1] == 8 and coords[1] + len(mot) >= 8)):
                    verification = False
                    
        
        direction = ""
        POSSIBILITE = ["horizontale","verticale"]
        if premiertour and coords != [8,8]:
            if coords[0] == 8 :
                direction = 'verticale'
            else:
                direction = 'horizontale'
        else:
            while direction.lower() not in POSSIBILITE:
                affichage_ecran(board,joueurs,ordre,sac)
                print("Dans quelle direction ? (horizontale/verticale)")
                direction = input("> ")

        
        #print(comptage(board,mot,direction,coords[0]-1,coords[1]-1))
        #time.sleep(4)

        placer_mot(board, main, mot.upper(), coords[1]-1, coords[0]-1, direction.lower())

        #REMETTRE LE NOMBRE DE PIECES POSER DANS LA MAIN DU JOUEURS
        completer_main(main,sac)
    
    
        prochain_tour(board, ordre, joueurs, sac,liste_mots, False)

"""#VARIABLES TEMPORAIRES DE TEST    
lettres = init_dico()
sac = init_pioche(lettres)
board = board()
liste_mots = generer_dico()
#----------------------------------
clear_screen()
joueurs = initialisation(sac)
ordre = 0
init_bonus(board)
#sac = ['R','O','B','I','N','E','T']
tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre, premiertour=False)"""
