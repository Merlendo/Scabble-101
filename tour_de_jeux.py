from pioche import piocher, init_dico, init_pioche, echanger, completer_main
from plateau import affichageBoard, init_bonus, board
from placement import lire_coords, tester_placement, placer_mot, coords_check
from construction_mots import mot_jouable, generer_dico, mots_jouables
import os

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

def fin_partie():
    return None

def prochain_tour(board, ordre, joueurs, sac):
    ordre = (ordre+1)%len(joueurs)
    tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre)

def affichage_ecran(board,joueurs,ordre,sac):
    clear_screen()
    affichageBoard(board)
    print("NOM DU JOUEUR :", joueurs[ordre]["nom"])
    print(["A","Z","E","V","C","?","U"])
    #print(joueurs[ordre]["main"])
    print("TAILLE SAC :", len(sac))

def tour_joueur(board, main, sac, joueurs, ordre):
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
        prochain_tour(board, ordre, joueurs, sac)

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

        prochain_tour(board, ordre, joueurs, sac)
    
    #PLACE DES JETONS - TESTER LES FONCTION DU MODULES PLACEMENT
    elif action == "3":

        main = ["A","Z","E","V","C","?","U"]
        verification = True
        #REPARER VERIFICATION
        while verification:
            affichage_ecran(board,joueurs,ordre,sac)
            motsJouable = mots_jouables(liste_mots,main)
            print(motsJouable[:5])

            print("Quelle mot voulez vous placer ?")
            mot = input("> ")
            if mot.upper() in motsJouable:
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
                verification = False
        
        direction = ""
        POSSIBILITE = ["horizontale","verticale"]
        while direction.lower() not in POSSIBILITE:
            affichage_ecran(board,joueurs,ordre,sac)
            print("Dans quelle direction ? (horizontale/verticale)")
            direction = input("> ")
            
       
        placer_mot(board, main, mot.upper(), coords[1]-1, coords[0]-1, direction.lower())

        #REMETTRE LE NOMBRE DE PIECES POSER DANS LA MAIN DU JOUEURS
        completer_main(main,sac)
    
    
        prochain_tour(board, ordre, joueurs, sac)

#VARIABLES TEMPORAIRES DE TEST    
lettres = init_dico()
sac = init_pioche(lettres)
board = board()
liste_mots = generer_dico()
#----------------------------------
clear_screen()
joueurs = initialisation(sac)
ordre = 0
init_bonus(board)
tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre)
