import random

lst_predef = ["bonjour", "salut", "nouveau", "partage", "demande", "avancer", "rouge"]

mot_a_deviner = random.choice(lst_predef)
print("Mot à deviner :\t", "-"*len(mot_a_deviner))
mot_evolue = list("-"*len(mot_a_deviner))
chance = 3
while chance <= 3 :
    letre_a_deviner = input("devine un lettre dans le mot caché : ")
    indice = mot_a_deviner.find(letre_a_deviner)
    if indice == -1 :
        chance -= 1
        print(letre_a_deviner, "n'est pas dans le mot à deviner")
        print("Reste de nombre de vie : ", chance)
    else :
        x = dict(list(enumerate(mot_a_deviner)))
        for a, b in x.items():
            if b == letre_a_deviner :
                mot_evolue[a] = letre_a_deviner
        print("Mot à deviner :\t", "".join(mot_evolue))
        if "-" not in mot_evolue :
            print("___Bravo__")
            print("Le mot à deviner est : ", mot_a_deviner)
            break
    if chance == 0 :
        print("____Perdu___")
        print("Le mot à deviner est : ", mot_a_deviner)
        break