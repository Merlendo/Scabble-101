from construction_mots import generer_dico, mots_jouables
from pioche import init_dico

def valeur_mot(mot,dico):
    valeur=0
    for c in mot.upper():
        valeur=valeur + dico[c]["val"]
        
    return valeur

def valeur_mot_bonus(mot,dico,values_bonus,scrabble):
    valeur=0
    i=0
    for c in mot.upper():

        valeur=valeur + dico[c]["val"]*values_bonus[1][i]
        i=i+1
    if values_bonus[0][0]!=0:
        valeur=valeur*values_bonus[0][0]
    elif values_bonus[0][1]!=0:
        valeur=valeur*values_bonus[0][1]
    if scrabble:
        valeur=valeur+50
    
    return valeur


def meilleur_mot(liste_mots_possibles,lettres,dico):
    mots = mots_jouables(liste_mots_possibles,lettres)
    meilleurMot = mots[0]

    for mot in mots:
        if valeur_mot(mot,dico) > valeur_mot(meilleurMot,dico):
            meilleurMot = mot
    meilleursMots = []
    for mot in mots:
        if valeur_mot(mot,dico) == valeur_mot(meilleurMot,dico):
            meilleursMots.append(mot)
    return meilleursMots


"""lettres = init_dico()
dico=generer_dico()
main=["A","A","B","R","R","R","E","V","I","M","A","E","U","Y","S"]
best = meilleur_mot(dico,main,lettres)

print("Les mots les plus interressant sont :",best,"avec",valeur_mot(best[0],lettres),"points")"""

