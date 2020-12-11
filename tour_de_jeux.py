from pioche import piocher, init_dico, init_pioche, echanger
from plateau import affichageBoard, init_bonus, board
from placement import lire_coords, tester_placement, placer_mot

#VARIABLES TEMPORAIRES DE TEST    
lettres = init_dico()
sac = init_pioche(lettres)
board = board()
#----------------------------------

def initialisation(sac): 
    setup = dict()
    nombreDeJoueurs = int(input("Combien de joueur voulez-vous? : "))

    for i in range(nombreDeJoueurs):
        print("Nom du joueur",i,":")
        j = input()
        setup[i] = {'main': piocher(7,sac), 'score': 0, 'nom': j}
    return setup

def fin_partie():
    return None

def tour_joueur(board, main, sac, joueurs, ordre):
    #AFFICHAGE DU PLATEAU / ESTHETIQUE / MISE EN PLACE
    init_bonus(board)
    affichageBoard(board)
    print("NOM DU JOUEUR :", joueurs[ordre]["nom"])
    print(main)
    #-------------------------------------------------------#

    #ACTION DU TOURS
    action = 0
    POSSIBILITE = [1, 2, 3]
    while action not in POSSIBILITE:
        print("1 - PASSER | 2 - ECHANGER | 3 - PLACER")
        action = int(input("> "))
    
    #PASSE LE TOUR - OK
    if action == 1:
        ordre = (ordre+1)%len(joueurs)
        print("ORDRE", ordre)
        tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre)

    #ECHANGE DES JETONS - FAIRE LA SELECTIONS DES JETONS A ECHANGER
    elif action == 2:
        echanger(jetons, main, sac)

        ordre = (ordre+1)%len(joueurs)
        tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre)
    
    #PLACE DES JETONS - TESTER LES FONCTION DU MODULES PLACEMENT
    elif action == 3:
        coords = lire_coords()
        print("Quelle mot voulez vous placer ?")
        mot = input("> ")
        #  TESTER LE MOT AVEC LES FONCTIONS CONSTRUCTION_MOTS!!!

        tester_placement(board, coords[0], coords[1], direction, mot)


joueurs = initialisation(sac)
print(joueurs)

ordre = 0
tour_joueur(board, joueurs[ordre]["main"], sac, joueurs, ordre)
