from pioche import piocher, init_dico, init_pioche, echanger, completer_main
from plateau import affichageBoard, init_bonus, board
from placement import lire_coords, tester_placement, placer_mot, coords_check, comptage
from construction_mots import mot_jouable, generer_dico, mots_jouables
from valeurs import valeur_mot_bonus, valeur_mot
import os
import time
import shelve

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

def fin_partie(sac, joueurs,board,ordre):
    if len(sac) == 0:
        affichage_ecran(board,joueurs,ordre,sac)
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


        time.sleep(10)#menu()
        print("Appuyer sur Entrer pour quitter")
        input()
        clear_screen()
        exit()


def prochain_tour(board, ordre, joueurs, sac, liste_mots, premiertour):
    ordre = (ordre+1)%len(joueurs)
    tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre, liste_mots, premiertour)

def affichage_ecran(board,joueurs,ordre,sac):
    clear_screen()
    affichageBoard(board)
    print("LEGENDE : * : MOT TRIPLE | ^ : MOT DOUBLE | - : LETTRES TRIPLE | + : LETTRES DOUBLE")
    print("NOM DU JOUEUR :", joueurs[ordre]["nom"])
    #print(["A","Z","E","V","C","?","U"])

    for i in range(len(joueurs)):
        print(joueurs[i]['nom'] + ":",str(joueurs[i]['score']) + " | ", end='', sep=" ")
    print()
    print(joueurs[ordre]["main"])
    print("TAILLE SAC :", len(sac))

def tour_joueur(board, main, sac, joueurs, ordre, liste_mots, premiertour):
    fin_partie(sac, joueurs,board,ordre)
    
    #AFFICHAGE DU PLATEAU 
    affichage_ecran(board,joueurs,ordre,sac)

    #ACTION DU TOURS
    action = 0
    POSSIBILITE = ["1", "2", "3","4"]
    while action not in POSSIBILITE:
        affichage_ecran(board,joueurs,ordre,sac)
        print("1 - PASSER | 2 - ECHANGER | 3 - PLACER | 4 - SAUVEGARDER")
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
                if not premiertour or ((coords[0] == 8 and coords[1]-1 + len(mot) >= 8) or (coords[1] == 8 and coords[0]-1 + len(mot) >= 8)):
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
       
       
        #----------------------------------------------------------------------------------------------------------------
        ## TENTATIVE DE VALEUR
        lettres = init_dico()
        print("VALEUR MOT : ",valeur_mot(mot,lettres))
        time.sleep(5)
        lettres_necessaires=tester_placement(board,coords[1]-1,coords[0]-1,direction,mot)
        if len(lettres_necessaires)!=0:
            compte_bonus=comptage(board,mot,direction,coords[1]-1, coords[0]-1)
            placer_mot(board, main, mot.upper(), coords[1]-1, coords[0]-1, direction.lower(),lettres_necessaires)
            scrabble=completer_main(main,sac)
            joueurs[ordre]["score"]=joueurs[ordre]["score"]+valeur_mot_bonus(mot,lettres,compte_bonus,scrabble)
        
        #----------------------------------------------------------------------------------------------------------------
        
        #placer_mot(board, main, mot.upper(), coords[1]-1, coords[0]-1, direction.lower())

        #REMETTRE LE NOMBRE DE PIECES POSER DANS LA MAIN DU JOUEURS
        #completer_main(main,sac)
    
    
        prochain_tour(board, ordre, joueurs, sac,liste_mots, False)

    elif action == '4':
        affichage_ecran(board,joueurs,ordre,sac)
        print("Entrer le nom de votre sauvegarde :")
        nom = input("> ")
        #(board, main, sac, joueurs, ordre, liste_mots, premiertour
        os.mkdir("SAVE/"+nom)
        sauvegarde = shelve.open("SAVE/"+nom+'/'+nom)
        sauvegarde['plateau'] = board
        sauvegarde['sac'] = sac
        sauvegarde['joueurdic'] = joueurs
        sauvegarde['ordre'] = ordre
        sauvegarde['premiertour'] = premiertour
        sauvegarde.close()
        exit()
