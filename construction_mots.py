def generer_dico():
    f=open('dico.txt','r')
    dico_final=[]
    for line in f:
        dico_final.append(line.rstrip())
    return dico_final

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

def mots_jouables(liste_mots,lettres):
    v=[]
    for i in liste_mots:
        if mot_jouable(i,lettres):
            v.append(i)
    return v
