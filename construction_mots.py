#Genere la liste des mots possibles au scrabble d'après le fichier dico.txt
def generer_dico():
    f=open('dico.txt','r')
    dico_final=[]
    for line in f:
        dico_final.append(line.rstrip())
    return dico_final

#Renvoi un booléen si le mot est jouable selon la main du joueur
def mot_jouable(mot,ll):
    lettres = list(ll)
    possible = True
    for i in mot :
        possible = possible and (i in lettres)
        if possible :
            lettres.remove(i)
        elif '?' in lettres :
                lettres.remove('?')
                possible = True

    return possible

#Renvoi une liste de mots jouables selon la main du joueurs
def mots_jouables(liste_mots,lettres):
    v=[]
    for i in liste_mots:
        if mot_jouable(i,lettres):
            v.append(i)
    return v
