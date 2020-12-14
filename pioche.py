import random

#Petit script qui ma servi à simplifié la création du dictionnaire (inutile au programme, mais peut-être utile si on veux modifié l'occurence ou la valeur des lettre ? Selon la langue par exemple)
def init_dico_manuel():
    lettres = dict()
    i = ord("A")
    while i <= ord("Z"):
        lettres[chr(i)] = {}
        i = i + 1
    lettres["?"] = {}
    print(lettres)
    for lettre in lettres:
        print(lettre)
        occ = int(input("Occurance : "))
        val = int(input("Valeur : "))
        lettres[lettre] = {"occ" : occ, "val" : val}
        print("deuxieme dic : ",lettres[lettre])
    return lettres

#Dictionnaire d'occurence et de valeurs des lettres
def init_dico():
    lettres = {'A': {'occ': 9, 'val': 1},
               'B': {'occ': 2, 'val': 3}, 
               'C': {'occ': 2, 'val': 3}, 
               'D': {'occ': 3, 'val': 2}, 
               'E': {'occ': 15, 'val': 1}, 
               'F': {'occ': 2, 'val': 4}, 
               'G': {'occ': 2, 'val': 2}, 
               'H': {'occ': 2, 'val': 4}, 
               'I': {'occ': 8, 'val': 1}, 
               'J': {'occ': 1, 'val': 8}, 
               'K': {'occ': 1, 'val': 10}, 
               'L': {'occ': 5, 'val': 1}, 
               'M': {'occ': 3, 'val': 2}, 
               'N': {'occ': 6, 'val': 1}, 
               'O': {'occ': 6, 'val': 1}, 
               'P': {'occ': 2, 'val': 3}, 
               'Q': {'occ': 1, 'val': 8}, 
               'R': {'occ': 6, 'val': 1}, 
               'S': {'occ': 6, 'val': 1}, 
               'T': {'occ': 6, 'val': 1}, 
               'U': {'occ': 6, 'val': 1}, 
               'V': {'occ': 2, 'val': 4}, 
               'W': {'occ': 1, 'val': 10}, 
               'X': {'occ': 1, 'val': 10}, 
               'Y': {'occ': 1, 'val': 10}, 
               'Z': {'occ': 1, 'val': 10}, 
               '?': {'occ': 2, 'val': 0}}

    return lettres

#Créer la pioche/sac
def init_pioche(dico):
    pioche = []
    for lettre in dico :
        for i in range(dico[lettre]["occ"]):
            pioche.append(lettre)
        #pioche = [lettre for x in range(dico[lettre]["occ"])] VOIR COMPREHENSION PYTHON
    return pioche

#Permet de piocher un nombre de pièce dans le sac
def piocher(x, sac):
    jetons_piocher = []
    for i in range(x):
        r = random.randint(0,len(sac)-1)
        jetons_piocher.append(sac[r])
        sac.pop(r)
    return jetons_piocher

#Complete la main du joueur
def completer_main(main,sac):
    scrabble=False
    jeton_a_piocher = 7-len(main)


    if len(sac) <= jeton_a_piocher:
        main.extend(piocher(len(sac),sac))

    else:
        main.extend(piocher(jeton_a_piocher,sac))
    
    #Renvoi True si le joueur a fait un SCRABBLE et est traité dans valeur_mot_bonus()
    if jeton_a_piocher==7:
        scrabble=True
        
    return scrabble

#Echange une liste de jeton entre le sac et la main du joueur, on enlève les jetons sélectionner de la main du joueur dans tour_de_jeu
def echanger(jetons, main, sac):
    listeJeton = piocher(len(jetons),sac)
    main.extend(listeJeton)
    sac.extend(jetons)
