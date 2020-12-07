print()
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


##fonction part 3

def generer_dico():
    f=open('dico.txt','r')
    dico_final=[]
    for line in f:
        dico_final.append(line.rstrip())
    return dico_final

def mot_jouable(mot,lettres):
    liste_lettre=list(lettres)
    i=0
    compte=0
    possible=False
    for i in liste_lettre:
        if i.upper() in mot.upper() or i.upper=='':
            compte=compte+1

    if compte>=len(mot):
        possible=True
    return possible
    
def mots_jouables(liste_mots,lettres):
    v=[]
    for i in liste_mots:
        a=mot_jouable(i,lettres)
        if a==True:
            v.append(i)
    return v

##Fin fonction part 3
dico=generer_dico()

def valeur_mot(mot,val_lettres):
    mot_1=list(mot.upper())
    valeur=0
    for i in mot_1:
        valeur=valeur + val_lettres[i]["val"]
        valf=valeur
        
    ##print("valeur du mot=",valeur)
    if len(mot_1)==7:
        valf=valf+50
        ##print("scrabble, +50 pts :",valf)
    return valf


def meilleur_mot(liste_mots_possibles,lettres,val_lettres):
    liste=mots_jouables(liste_mots_possibles,lettres)
    Max={"maxi":{"mot":"","val":0}}
    ind=1
    for j in liste:
        v=valeur_mot(j,val_lettres)
        if v > Max["maxi"]["val"]:
            Max["maxi"]["mot"]=j
            Max["maxi"]["val"]=v
        elif v==Max["maxi"]["val"]:
            Max["maxi"+str(ind)]={"mot"+str(ind):j,"val":v}
            ind=ind+1
    maximum = Max["maxi"]["val"]
    Mix=dict(Max)
    for i in Max:
        if Max[i]['val']<maximum:
            del Mix[i]
    
    return Mix

main=["a","a","b"]
plus_mieux=meilleur_mot(dico,main,lettres)

for elem in plus_mieux:
    print("Le mot le plus interressant est :",plus_mieux[elem]["mot"],"avec",plus_mieux[elem]["val"],"points")
