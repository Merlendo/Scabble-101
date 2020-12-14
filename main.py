from pioche import init_dico, init_pioche
from plateau import init_bonus, board
from construction_mots import generer_dico
from tour_de_jeux import initialisation, tour_joueur
import os
import shelve

def affichage():
    os.system('cls')
    art = """   _____ __________  ___    ____  ____  __    ______
  / ___// ____/ __ \/   |  / __ )/ __ )/ /   / ____/
  \__ \/ /   / /_/ / /| | / __  / __  / /   / __/   
 ___/ / /___/ _, _/ ___ |/ /_/ / /_/ / /___/ /___   
/____/\____/_/ |_/_/  |_/_____/_____/_____/_____/   
                                                    """

    print('#---------------------------------------------------#\n')
    print(art)
    print('\n#---------------------------------------------------#\n')

def menu():
    action = 0
    POSSIBILITE = ["1", "2", "3"]
    while action not in POSSIBILITE:
        affichage()
        print("1 - JOUER | 2 - CHARGER | 3 - QUITTER")
        action = input("> ")

    if action == '1':
        #  INITIALISATION VARIABLES 
        lettres = init_dico()
        sac = init_pioche(lettres)
        b = board()
        liste_mots = generer_dico()
        #----------------------------------
        joueurs = initialisation(sac)
        ordre = 0
        init_bonus(b)
        sac = ['R','O','B','I','N','E','T']
        tour_joueur(b, joueurs[ordre]["main"], sac, joueurs, ordre, liste_mots, True)
    
    if action == '2':
        print("Entrer le nom de votre sauvegarde :")
        nom = input("> ")

        #(board, main, sac, joueurs, ordre, liste_mots, premiertour
        sauvegarde = shelve.open("SAVE/"+nom+'/'+nom)
        b = sauvegarde['plateau'] 
        sac = sauvegarde['sac'] 
        joueurs = sauvegarde['joueurdic'] 
        ordre = sauvegarde['ordre'] 
        premiertour = sauvegarde['premiertour']
        sauvegarde.close()

        liste_mots = generer_dico()
        tour_joueur(b, joueurs[ordre]["main"], sac, joueurs, ordre, liste_mots, premiertour)

    if action == '3':
        os.system('cls')
        exit()

menu()
