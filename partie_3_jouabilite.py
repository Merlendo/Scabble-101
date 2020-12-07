def generer_dico():
    f=open('dico.txt','r')
    dico_final=[]
    for line in f:
        dico_final.append(line.rstrip())
    return dico_final
print(generer_dico())

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

liste=['mordo','ourir','courrir','mourir','valhala']
l1=['o','u','R','r','','c','i']  
print ('main:',l1)
print('possibilités:',mots_jouables(liste,l1))
