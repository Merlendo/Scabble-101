from construction_mots import generer_dico, mots_jouables
from pioche import init_dico

def valeur_mot(mot,dico):
    valeur=0
    for c in mot.upper():
        valeur=valeur + dico[c]["val"]
        
    return valeur


def meilleur_mot(liste_mots_possibles,lettres,dico):
    mots = mots_jouables(liste_mots_possibles,lettres)
    meilleurMot = mots[0]

    for mot in mots:
        if valeur_mot(mot,dico) > valeur_mot(meilleurMot,dico):
            meilleurMot = mot
    return meilleurMot

lettres = init_dico()
dico=generer_dico()
main=["A","A","B","R","R","R","E","V","I","M"]
best = meilleur_mot(dico,main,lettres)
print("Le mot le plus interressant est :",best,"avec",valeur_mot(best,lettres),"points")

