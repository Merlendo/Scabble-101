import random

def init_dico_manuel():
    lettres = dict()
    i = ord("A")
    while i <= ord("Z"):
        lettres[chr(i)] = {}
        i = i + 1
    lettres["?"] = {}
    print(lettres)
    for lettre in lettres:
        print(lettre)
        occ = int(input("Occurance : "))
        val = int(input("Valeur : "))
        lettres[lettre] = {"occ" : occ, "val" : val}
        print("deuxieme dic : ",lettres[lettre])
    return lettres


def init_dico():
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

    return lettres

def init_pioche(dico):
    pioche = []
    for lettre in dico :
        for i in range(dico[lettre]["occ"]):
            pioche.append(lettre)
        #pioche = [lettre for x in range(dico[lettre]["occ"])] VOIR COMPREHENSION PYTHON
    return pioche

def piocher(x, sac):
    jetons_piocher = []
    for i in range(x):
        r = random.randint(0,len(sac)-1)
        jetons_piocher.append(sac[r])
        sac.pop(r)
    return jetons_piocher

def completer_main(main,sac):
    jeton_a_piocher = 7-len(main)
    if len(sac) <= jeton_a_piocher:
        main.extend(piocher(len(sac),sac))
    else:
        main.extend(piocher(jeton_a_piocher,sac))
        
def echanger(jetons, main, sac):
  return None
    

dico = init_dico()
p = init_pioche(dico)
print(p)
pioche = ['A']
main = ["I","J"]
print(main)
completer_main(main,pioche)
print(pioche)
print(main)
