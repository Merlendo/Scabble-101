
## partie 1

def init_bonus():

    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]

    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

    cases ={ 'MT': cases_MT ,'MD' : cases_MD , 'LT' : cases_LT , 'LD': cases_LD}

    l = []
    
    for i in range(15):

        ll=[]

        for j in range (15):
            n = len(ll)
            for e in cases :
                
                if [i,j] in cases[e]:
                    ll.append(e)
            if len(ll) == n:
                ll.append(' ')
                
        l.append(ll)

    return l

def init_jetons():
    x=[["" for j in range(15)] for i in range(15)]
    return x
#print (init_jetons())
    
def affiche_jetons(j,x) : # prosoire 

    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]

    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]    

    caseb = { '*': cases_MT ,'^' : cases_MD , '-' : cases_LT , '+': cases_LD}

    # utiliser la fonction init_bonus()
    

    cases = []
    li = 0
    for ligne in init_jetons() :
        
        lignes = []
        el = 0
        for elem in ligne :

            if [li,el] in j :
                
                n = len(lignes)
                for c in caseb :
                    if [li,le] in case[c] :
                        lignes.append(x+c)

                if len(lignes) == n:
                    lignes.append(x)

            else:
                lignes.append(elem)
            li = li + 1
        cases.append(lignes)
        el = el+1

    for i in cases :
        for k in i :
            print(k.rjust(1),end=' ')
        print('')


## partie 2

import random as r

def init_dico():
    
    dico = {
        "A": { "occ" : 9 , "val" : 1},
        "B": { "occ" : 2 , "val" : 3},
        "C": { "occ" : 2 , "val" : 3},
        "D": { "occ" : 3 , "val" : 2},
        "E": { "occ" : 15, "val" : 1},
        "F": { "occ" : 2 , "val" : 4},
        "G": { "occ" : 2 , "val" : 2},
        "H": { "occ" : 2 , "val" : 4},
        "I": { "occ" : 8 , "val" : 1},
        "J": { "occ" : 1 , "val" : 8},
        "K": { "occ" : 1 , "val" : 10},
        "L": { "occ" : 5 , "val" : 1},
        "M": { "occ" : 3 , "val" : 2},
        "N": { "occ" : 6 , "val" : 1},
        "O": { "occ" : 6 , "val" : 1},
        "P": { "occ" : 2 , "val" : 3},
        "Q": { "occ" : 1 , "val" : 8},
        "R": { "occ" : 6 , "val" : 1},
        "S": { "occ" : 6 , "val" : 1},
        "T": { "occ" : 6 , "val" : 1},
        "U": { "occ" : 6 , "val" : 1},
        "V": { "occ" : 2 , "val" : 4},
        "W": { "occ" : 1 , "val" : 10},
        "X": { "occ" : 1 , "val" : 10},
        "Y": { "occ" : 1 , "val" : 10},
        "Z": { "occ" : 1 , "val" : 10},
        "?": { "occ" : 2 , "val" : 0},
    }

    return dico

def init_pioche(dico):

    pioche=[]

    for i in range(26):

        pos = chr(ord('A')+i)

        l=dico[pos]
        
        pioche.extend(pos*l['occ'])

    l=dico['?']

    pioche.extend('?'*l['occ']) 

    return pioche

def piocher(x, sac):

    l=[]

    for i in range(0,x):

        a = r.randint(0,len(sac)-1)

        l.append(sac.pop(a))
                    

    return l

def completer_main(main,sac):
    

    n = 7-len(main)
    
    if len(sac)-n >= 0 :
        
        main.extend(piocher(n,sac))

    else :

        main.extend(piocher(len(sac),sac))

def echanger(jetons, main, sac):

    for i in jetons:

        main.remove(i)

    l = piocher(len(jetons),sac)
    main.extend(l)

    sac.extend(jetons)


## partie 3

def genere_dico(nf):
    
    with open(nf) as f:
        mots = [ligne.rstrip() for ligne in f]
        
    return mots

def mot_jouable(mot, ll):
    
    l = list(ll)
    ok = True
    
    for i in mot :
    
        ok = ok and (i in l )
    
        if ok :
            l.remove(i)
            
        elif '?' in l :
                l.remove('?')
                ok = True
        
    return ok


def mots_jouable(motsfr,ll): ## exploter les mots deja présent

    mj = []

    for i in motsfr:
        
        if mot_jouable(i,ll):

            mj.append(i)
    
    

    return mj


## partie 4

def valeur_mot(mot,dico):

    val = 0

    for i in mot :
        
        val = val + dico[i]['val']

    return val

def meilleur_mot(motsfr, ll, dico):

    mots = mots_jouable(motsfr,ll)

    lm =[]

    mm = valeur(mots[0] ,dico)

    for m in mots:
        
        if mm < valeur_mot(m,dico) :
        
            mm = valeur_mot(m,dico)

    for m in mots:   # boucle option 

        if valeur(m,dico) == mm :

            lm.append(m)

    return lm



## partie 5

def lire_coords():

    i = int(input("donner la ligne ou vous voulez placer le jetons "))
    while i<0 or i>14 :
        i = int(input("donner la ligne ou vous voulez placer le jetons "))
    j = int(input("donner la colone ou vous voulez placer le jetons "))
    while j<0 or j>14 :
        j = int(input("donner la colone ou vous voulez placer le jetons "))

    return i,j

def tester_placement(plateau,i,j,dr,mot):

    ok = True
    l = []

    if dr == "horizontal":

        if len(mot) > 14 - j:
            ok = False
        else :
            for x in range(j,15):
                if plateau[i,x]!= '' or plateau [i,x]!= mot[x-j]:
                    ok = False

        if ok :  
            x = j
            for e in mot :
                if plateau[i,x] == '' :
                    l.append(e)
                x = x+1
                    
    if dr == "vertical":

        if len(mot) > 14 - i:
            ok = False
        else :
            for x in range(i,15):
                if plateau[x,j]!= '' or plateau [x,j]!= mot[x-i]:
                    ok = False

        if ok :  
            x = i
            for e in mot :
                if plateau[x,j] == '' :
                    l.append(e)
                x = x+1
    return l

def placer_mot(plateau,lm,mot,i,j,dr):
    
    l = tester_placement(plateau,i,j,dr,mot)
    
    
    if len(l)!= 0 :
        
        if dr == "horizontal":
            x = j
            for e in mot :
                if e in l :
                    plateau[i,x] = e
                    lm.remove(e)
                x = x + 1
        if dr == "vertical":
            x = i
            for e in mot :
                if e in l :
                    plateau[x,j] = e
                    lm.remove(e)
                x = x + 1
        ok = True
    else :
        ok = False
        
    return ok


## partie 6



## programme principale

# premier tour 
print("vous disposer du plateau suivant")

for i in init_bonus(): # afficher plateau avec bonus
    for j in i :
        print(j.rjust(1),end=' ')
    print('')

init_jetons()
sac = init_pioche(init_dico())
main1 = piocher(7,sac)
main2 = piocher(7,sac)

