#partie1

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
                ll.append('  ')
                
        l.append(ll)

    return l

def init_jetons():
    x=[["" for j in range(15)] for i in range(15)]
    return x

def affiche_jetons(j) :

    cb = init_bonus()

    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]

    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

    caseb = { '*': cases_MT ,'^' : cases_MD , '-' : cases_LT , '+': cases_LD}

    cases = []
    li = 0

    for ligne in j :

        lignes = []
        el = 0

        for elem in ligne :

            if elem != '' :

                n = len(lignes)
                for c in caseb :
                    if [li,el] in caseb[c] :
                        lignes.append(elem+c)

                if len(lignes) == n:
                    lignes.append(elem+' ')

            else:
                lignes.append(cb[li][el])
            el = el + 1

        cases.append(lignes)
        li = li + 1


    print('',end='')
    for i in range(15):
        print(str(i).rjust(2),end=' ')
    print('')
    lig = 0
    for i in cases :
        
        for k in i :
            print(k.rjust(1),end=' ')
        
        print(str(lig).rjust(1),end=' ')
        lig = lig + 1
        print(' ')

# partie2
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

        del main[main.index(i)]

    l = piocher(len(jetons),sac)
    main.extend(l)

    sac.extend(jetons)

#partie3

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

def mot_possible(mot,ll):
    
    l = list(ll)
    ok = True
    
    for i in mot :
        ok = ok and (i in l )
        if ok :
            l.remove(i)
    return ok

def mots_jouables(motsfr,ll):

    mj = []

    for i in motsfr:
        
        if mot_possible(i,ll):

            mj.append(i)

    return mj

#partie4

def valeur_mot(mot,dico):

    val = 0

    for i in mot :
        
        val = val + dico[i]['val']

    return val

def meilleur_mot(motsfr, ll, dico):

    mots = mots_jouables(motsfr,ll)

    lm =[]

    mm = valeur_mot(mots[0] ,dico)

    for m in mots:
        
        if mm < valeur_mot(m,dico) :
        
            mm = valeur_mot(m,dico)

    for m in mots:   # boucle option 

        if valeur_mot(m,dico) == mm :

            lm.append(m)

    return lm

#partie5

def lire_coords():

    i = int(input("donner la ligne ou vous voulez placer le jetons "))
    while i<0 or i>14 :
        i = int(input("donner la ligne ou vous voulez placer le jetons "))
    j = int(input("donner la colone ou vous voulez placer le jetons "))
    while j<0 or j>14 :
        j = int(input("donner la colone ou vous voulez placer le jetons "))

    return [i,j]

def tester_placement(plateau,i,j,dr,mot):

    ok = True
    l = []

    if dr == "horizontale":

        if len(mot) > 15 - j:
            ok = False
        else :
            for x in range(j,j+len(mot)):
                if not( plateau[i][x]=='' or plateau [i][x]== mot[x-j]):
                    ok = False

        if ok :  
            x = j
            for e in mot :
                if plateau[i][x] == '' :
                    l.append(e)
                x = x+1
                    
    if dr == "verticale":

        if len(mot) > 15 - i:
            ok = False
        else :
            for x in range(i,i+len(mot)):
                if not( plateau[x][j]=='' or plateau [x][j]== mot[x-i]):
                    ok = False

        if ok :  
            x = i
            for e in mot :
                if plateau[x][j] == '' :
                    l.append(e)
                x = x+1
    return l

def placer_mot(plateau,lm,mot,i,j,dr):
    
    l = tester_placement(plateau,i,j,dr,mot)
    
    
    if len(l)!= 0 :
        
        if dr == "horizontale":
            x = j
            for e in mot :
                if e in l :
                    plateau[i][x] = e
                    if e not in lm and '?' in lm :
                        lm.remove('?')
                    else:
                        lm.remove(e)
                x = x + 1
        if dr == "verticale":
            x = i
            for e in mot :
                if e in l :
                    plateau[x][j] = e
                    if e not in lm and '?' in lm :
                        lm.remove('?')
                    else:
                        lm.remove(e)
                x = x + 1
        ok = True
    else :
        ok = False
        
    return ok

def valeur_bonus(plateau,mot,i,j,dico,bonus,dr):

    val = valeur_mot(mot,dico)
    

    if dr == "horizontale":

        for x in range(j,j+len(mot)):

            lettre = plateau[i][x]

            if bonus[i][x] == 'MT':

                val = val*3
                bonus[i][x] = ''
                    
            elif bonus[i][x] == 'MD' :

                val = val*2
                bonus[i][x] = ''

            elif bonus[i][x] == 'LT' :

                val = val + 2*dico[lettre]["val"]
                bonus[i][x] = ''

            elif bonus[i][x] == 'LT' :

                val = val + dico[lettre]["val"]
                bonus[i][x] = ''


    if dr == "verticale":
        
        for x in range(i,i+len(mot)):

            lettre = plateau[x][j]

            if bonus[x][j] == 'MT':

                val = val*3
                bonus[x][j] = ''
                    
            elif bonus[x][j] == 'MD' :

                val = val*2
                bonus[x][j] = ''

            elif bonus[x][j] == 'LT' :

                val = val + 2*dico[lettre]["val"]
                bonus[x][j] = ''

            elif bonus[x][j] == 'LT' :

                val = val + dico[lettre]["val"]
                bonus[x][j] = ''
                
    return val

#partie6

def joker(mot,lm):

    liste = list(mot)
    i = 0
    if '?' in lm:

        while i<len(liste):

            if liste[i].upper() not in lm:
                liste.pop(i)
                liste.insert(i,'?')
            i = i + 1
            
    mot = ''.join(liste).upper()




def demande_coup():

    coup = input('passer,echanger ou placer ? ' )
    coup = coup.lower()

    while not (coup=='passer' or coup=='echanger' or coup=='placer'):
        coup = input('passer,echanger ou placer ? ' )
        coup = coup.lower() 
  
    return coup  

def demande_mot(motsfr,lm):

    mot = input("mot a jouer : ")
    mot = mot.upper()
    while (mot not in motsfr) or not mot_jouable(mot,lm) :
        mot = input("mot a jouer : ")
        mot = mot.upper()
    return mot

def demande_direction():
    dr = input('horizontale ou verticale:  ')
    while not (dr =='horizontale' or dr == 'verticale'):
        dr = input('horizontale ou verticale:  ')
        
    return dr

def demande_aide(motsfr, lm, dico,sac):
    aide = input("voulez vous de l'aide ?\n oui,non : ")
    if aide == 'oui' :
        lm2=[i for i in lm]
        if len(meilleur_mot(motsfr, lm2, dico)) != 0:
            print(meilleur_mot(motsfr, lm2, dico))
        else :
            jetons = demande_echange(lm)
            echanger(jetons, lm, sac)
            print(lm,'\n')


def demande_echange(lm):
        
    
    
    jetons = input("donnez les jetons a echanger: ")
    jetons = jetons.upper()

    while not all(j in lm for j in jetons):#fct all verifie si tout les bool valent vrai
        # https://stackoverflow.com/questions/5217489/check-if-a-predicate-evaluates-true-for-all-elements-in-an-iterable-in-python
        jetons = input("donnez les jetons a echanger: ")
        jetons = jetons.upper()
    
    return jetons    

def tour_joueur(plateau,lm,bonus,dico,sac,motsfr):
    
    score = 0

    coup = demande_coup()

    if coup != 'passer':
        
        if coup == 'echanger':

            jetons = demande_echange(lm)
            echanger(jetons, lm, sac)
            print(lm,"\n\n")
            
        elif coup=='placer':

            demande_aide(motsfr, lm, dico,sac)
            mot = demande_mot(motsfr,lm)
            joker(mot,lm)
            print(mot)
            print("la valeur de ce mot est ", valeur_mot(mot,dico))
            i,j = lire_coords()
            dr = demande_direction()
            
            if tester_placement(plateau, i, j, dr, mot):
                placer_mot(plateau,lm,mot,i,j,dr)
                joker(mot,lm)
                score=valeur_bonus(plateau,mot,i,j,dico,bonus,dr)
            
            affiche_jetons(plateau)

    return score

def intheend (sac,main):

    completer_main(main,sac)
    
    return len(sac)== 0

def jnext(next,dljoueur):
    for e in dljoueur:
        next=dljoueur[e]['place']
    return next




## programme principal


from fonction import *

nbj = int(input("entrez le nombre de joueur "))
while nbj<2:
    nbj = int(input("entrez le nombre de joueur "))


dico = init_dico()
sac = init_pioche(dico)

plateau = init_jetons()
bonus = init_bonus()
motsfr = genere_dico('littre.txt')


lj=[]
    
for n in range(nbj) :

    d={}
    nom = input("donner le nom du joueur ")
    d['nom'] = nom 
    d['main'] = piocher(7,sac)
    
    d['score'] = 0

    lj.append(d)

affiche_jetons(plateau)


i = 0

while not intheend (sac,lj[i]['main']):

    print("tour du joueur ",lj[i]['nom'])
    print("jetons dans le sac: ",len(sac))
    print("score actuelle: ",lj[i]['score'])
    
    lm = lj[i]['main']
    print(lm)
    
    s = tour_joueur(plateau, lm, bonus, dico, sac,motsfr)

    lj[i]['score'] = lj[i]['score'] + s

    if len(lj[i]['main'])==0 : # regle du scrable
        lj[i]['score'] += 50

    print("score apres coup: ",lj[i]['score'])
    print("main apres coup ",lj[i]['main'])
    print('\n\n')

    i = (i+1)%nbj























