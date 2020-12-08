def generer_dico():
    f=open('dico.txt','r')
    dico_final=[]
    for line in f:
        dico_final.append(line.rstrip())
    return dico_final
#print(generer_dico())

def mot_jouable(mot,lettres):
    """liste_lettre = list(lettres)
    compte=0
    possible=False
    for i in liste_lettre:
        if i.upper() in mot.upper() or i.upper=='':
            compte=compte+1

    if compte>=len(mot):
        possible=True
    return possible
    """
    d1 = dict()
    for c in mot:
        d1[c.upper()] = d1.get(c.upper(),0) + 1
    #print(d1)

    d2 = dict()
    for c in lettres:
        d2[c.upper()] = d2.get(c.upper(),0) + 1
    #print(d2)
    possible = True
    for key in d1:
        #print(key,d2[key])
        if (key not in d2) or d1[key] > d2[key]:
            possible = False
    

    return possible

def mots_jouables(liste_mots,lettres):
    v=[]
    for i in liste_mots:
        a=mot_jouable(i,lettres)
        if a==True:
            v.append(i)
    return v

liste=generer_dico()
l1=['o','u','R','r','r','r','','c','i','M']  
print ('main:',l1)
print('possibilités:',mots_jouables(liste,l1))
print ('main:',l1)

"""l1=['u','R','r','r','','c','i']  
print(mot_jouable("ourir",l1))"""

