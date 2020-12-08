from pioche import piocher, init_dico, init_pioche

#VARIABLES TEMPORAIRES DE TEST    
lettres = init_dico()
sac = init_pioche(lettres)
#----------------------------------

def initialisation(sac): 
    setup = dict()
    nombreDeJoueurs = int(input("Combien de joueur voulez-vous? : "))

    for i in range(1,nombreDeJoueurs+1):
        print("Nom du joueur",i,":")
        j = input()
        setup[j] = {'main': piocher(7,sac), 'score': 0, 'ordre': i}
    return setup

def tour_joueur():
    

joueurs = initialisation(sac)
print(joueurs)
