from pioche import piocher, init_dico, echanger, completer_main
from plateau import affichageBoard
from placement import tester_placement, placer_mot, coords_check, comptage
from construction_mots import mots_jouables
from valeur import valeur_mot_bonus, valeur_mot, meilleur_mot
import os
import time
import shelve

def clear_screen():
    os.system('cls')

def initialisation(sac): 

    # Fonction d'initialisation des joueurs, stocke dans un dictionnaire leurs main, score et nom

    setup = dict()
    nombreDeJoueurs = int(input("Combien de joueur voulez-vous? : "))
    clear_screen()
    for i in range(nombreDeJoueurs):
        print("Nom du joueur",i+1,":")
        j = input("> ")
        setup[i] = {'main': piocher(7,sac), 'score': 0, 'nom': j}
        clear_screen()
    return setup

def fin_partie(sac, joueurs,board):

    #Detecte la fin de partie lorsque le sac n'a plus de pièces

    if len(sac) == 0:
        clear_screen()
        affichageBoard(board)
        print("La partie est fini")
        biggest = [joueurs[1]['nom'], joueurs[1]['score']]
        for i in range(len(joueurs)):
            print(joueurs[i]["nom"], ':',joueurs[i]["score"])
            if joueurs[i]["score"] > biggest[1]:
                biggest.insert(0, joueurs[i]['nom'])
                biggest.pop(1)
                biggest.insert(1, joueurs[i]['score'])
                biggest.pop(2)
        print("Le gagnant est ...",biggest[0],"avec",biggest[1], "points")


        time.sleep(10)
        print("Appuyer sur Entrer pour quitter")
        input()
        clear_screen()
        exit()


def prochain_tour(board, ordre, joueurs, sac, liste_mots, premiertour):
    
    #Change de tour en incrémentant la variable ordre et appelant la fonction tour_joueur
    
    ordre = (ordre+1)%len(joueurs)
    tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre, liste_mots, premiertour)

def affichage_ecran(board,joueurs,ordre,sac):

    # Affichage esthétique du plateau, du nom du joueurs actif, de la main, du score et de la taille du sac

    clear_screen()
    affichageBoard(board)
    print("LEGENDE :  * : MT  |  ^ : MD  |  - : LT  |  + : LD")

    print("\n-----------------------------------")
    print("NOM DU JOUEUR :", joueurs[ordre]["nom"])
    print("-----------------------------------")
    for i in range(len(joueurs)):
        print(joueurs[i]['nom'] + ":",str(joueurs[i]['score']) + " | ", end='', sep=" ")
    print()
    print("-----------------------------------")
    print(joueurs[ordre]["main"])
    print("-----------------------------------")
    print("TAILLE SAC :", len(sac))
    print("-----------------------------------\n")
def tour_joueur(board, main, sac, joueurs, ordre, liste_mots, premiertour):
    
    fin_partie(sac, joueurs,board)
    
    #AFFICHAGE DU PLATEAU 
    affichage_ecran(board,joueurs,ordre,sac)

    #ACTION DU TOURS
    action = 0
    POSSIBILITE = ["1", "2", "3","4"]
    while action not in POSSIBILITE:
        affichage_ecran(board,joueurs,ordre,sac)
        print("1 - PASSER | 2 - ECHANGER | 3 - PLACER | 4 - SAUVEGARDER")
        action = input("> ")
        

    #PASSE LE TOUR 
    if action == "1":
        prochain_tour(board, ordre, joueurs, sac,liste_mots,premiertour)

    #ECHANGE DES JETONS
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

        prochain_tour(board, ordre, joueurs, sac,liste_mots, premiertour)
    
    #PLACE DES JETONS
    elif action == "3":

        #Demande un mot au joueur temps jusqu'a ce qui corresponde à un mot possible au scrabble
        verification = True
        while verification:
            affichage_ecran(board,joueurs,ordre,sac)
            motsJouable = mots_jouables(liste_mots,main)
            print("Quelle mot voulez vous placer ?")
            mot = input("> ")

            #petit code pour appeler à l'aide pendant le choix du mot
            if mot == '!help':
                print(motsJouable[:5])
                time.sleep(4)
            elif mot == '!superhelp':
                if len(motsJouable) > 0:
                    print(meilleur_mot(motsJouable,main,init_dico()))
                else:
                    print("Aucun mot jouable")
                time.sleep(4)

            if mot.upper() in motsJouable or mot == "":
                verification = False
            
            #Remplace ? avec la lettre manquante
            templist = list(mot)
            if '?' in main:
                for i in range(len(templist)):
                    if templist[i].upper() not in main:
                        templist.pop(i)
                        templist.insert(i,'?')
            mot = ''.join(templist).upper()
                        
    
        #Demande les coordonnées une fois que le mot est vérifié
        verification = True
        while verification:

            affichage_ecran(board,joueurs,ordre,sac)
            print("Quelles coordonnées ? (ex : A5)")
            coords = input("> ")
            
            if coords_check(coords.upper()) != False:
                coords = coords_check(coords.upper())
                                        #permet d'obliger le placement du mot au milieu lors du premier tour 
                if not premiertour or ((coords[0] == 8 and coords[1]-1 + len(mot) >= 8) or (coords[1] == 8 and coords[0]-1 + len(mot) >= 8)):
                    verification = False 
                    
        #Demande la direction ou l'impose durant le premier tour
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

        
        #Attribue la valeur du placement du mot au score du joueur et place le mot
        #ATTENTION LES COORDONNEES POUR LES FONCTIONS compte_bonus, tester_placement, placer_mot SONT INVERSER PAR RAPPORT AUX COORDONNEES RENVOYE PAR check_coords
        lettres = init_dico()
        print("VALEUR MOT : ",valeur_mot(mot,lettres))
        time.sleep(3)
        lettres_necessaires=tester_placement(board,coords[1]-1,coords[0]-1,direction,mot)
        if len(lettres_necessaires)!=0:
            compte_bonus=comptage(board,mot,direction,coords[1]-1, coords[0]-1)
            placer_mot(board, main, mot.upper(), coords[1]-1, coords[0]-1, direction.lower(),lettres_necessaires)
            scrabble=completer_main(main,sac)
            joueurs[ordre]["score"]=joueurs[ordre]["score"]+valeur_mot_bonus(mot,lettres,compte_bonus,scrabble)
    
    
        #passe le tour
        prochain_tour(board, ordre, joueurs, sac,liste_mots, False)

    elif action == '4':

        #SAUVEGARDE

        #créer un dossier de sauvegarde dans le dossier SAVE et stocke dans des fichiers shelve les données du jeu à l'instant ou on appel cette action
        affichage_ecran(board,joueurs,ordre,sac)
        print("Entrer le nom de votre sauvegarde :")
        nom = input("> ")
        os.mkdir("SAVE/"+nom)
        sauvegarde = shelve.open("SAVE/"+nom+'/'+nom)
        sauvegarde['plateau'] = board
        sauvegarde['sac'] = sac
        sauvegarde['joueurdic'] = joueurs
        sauvegarde['ordre'] = ordre
        sauvegarde['premiertour'] = premiertour
        sauvegarde.close()
        clear_screen()
        exit()
