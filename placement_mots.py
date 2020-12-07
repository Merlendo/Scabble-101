""". Ecrire une fonction ´ lire coords() qui demande au joueur des coordonn´ees, les filtre jusqu’`a correspondre `a une
case vide du plateau, et les renvoie."""


def lire_coords():
    return coord = input("Entrez des coordonnées :")

"""Ecrire une fonction ´ tester placement(plateau,i,j,dir,mot) qui re¸coit le plateau, les coordonn´ees de la case de
placement de la premi`ere lettre, une direction (horizontal ou vertical), et un mot, et qui v´erifie si le mot est pla¸cable
`a cet endroit. Attention il peut y avoir d´ej`a des lettres pos´ees sur le plateau dont le mot fait usage. La fonction
renvoie la liste des lettres n´ecessaires pour placer ce mot `a cet endroit dans ce sens, ou bien une liste vide si c’est
impossible (par ex le mot est trop long, ou incompatible avec les lettres d´ej`a plac´ees...).
"""

def tester_placement(plateau,i,j,dir, mot):
