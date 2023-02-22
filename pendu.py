import random
#from pygame import *

# créer une liste de mots

mots = ["lion", "poummon", "athletisme", "football", "voiture", "informatique","justice",
       "etudiant", "estomac", "bouteille", "glace", "technicien"]

# je demande à l'ordinateur de choisir un mot au hasard par le modul random
ordinateur = random.choice(mots)

affichage = [] # je crée une liste vide qui contiendra tous les bonne lettre que l'utilisateur a déviné
for mot in ordinateur: # je parcours tous les mots fournit par l'ordinateur
    affichage.append("_") # j'ajoute le mot sur la liste vide affichage

erreur = 0 # initier le nombre à 0
vrai = False #on suppose que la lettre vide est faux tant que l'utilisateur n'a pas encore mis la lette
bonhome = [" "," "," "," "," "," "] # créer une liste pour le bonhome
bonhome_mort = ["o", "/", "|", "\\", "/", "\\"]

while not vrai:
    
    vrai = True
    print(" +---+")
    print(" |   |")
    print(" |   {}".format(bonhome[0]))
    print(" | {} {} {}".format(bonhome[1],bonhome[2],bonhome[3]))
    print(" |  {} {}".format(bonhome[4],bonhome[5]))
    print("_|_")
    print("| |")

     #mettre quelques indice pour le mot
    print("le mot contient: %s" %len(ordinateur), "lettres")
    if ordinateur == "lion":
        print("roi de la jungle")
    elif ordinateur == "poummon":
        print ("organe de la respiration")
    elif ordinateur == "athletisme":
        print("jeux olympique")
    elif ordinateur == "football":
        print("sport trés populaire")
    elif ordinateur == "voiture":
        print("permet de se déplacer")
    elif ordinateur == "informatique":
        print("premier support de la communication")
    elif ordinateur == "justice":
        print("désigne à faire corriger une inégalité, retablire l'ordre")
    elif ordinateur == "etudiant":
        print("il est tout temps sous préssion")
    elif ordinateur == "estomac": 
        print("organe de digestion")
    elif ordinateur == "bouteille":
        print("un recipien")
    elif ordinateur == "glace":
        print("elle se forme lors que l'eau passe  de l'état lique à l'état solide ")
    elif ordinateur == "technicien":
        print("il est abilité à etre sur le terrain")


    for utilisateur in ordinateur: # regarder si la lettre donner par l'utilisateur est present dant le mot choisit par l'ordinateur grace a random.choice 
        if utilisateur in affichage: # si la lettre est dans addiche
            print(utilisateur, end=" ") # on affiche la lettre
        else:
            vrai = False
            print("_", end=" ") #si non on met un _

     # si le nombre d'erreur est superieur à 5 le jeu  est terminé   
    if erreur > 5: 
        print( "tu as perdu! ")
        print("le mot était:%s" %ordinateur)
        break
    # si toutes les lettres sont trouvées, on affiche gagné    
    if vrai:
        print("bravo, tu as gagné!!!!!!!!! %s" %ordinateur )
        break
    
    # demander à l'utilisateur de deviner le mot
    utilisateur = input (" Trouvez le mot: ")
    affichage.append(utilisateur)

    if utilisateur not in ordinateur:
        bonhome[erreur] = bonhome_mort[erreur]
        erreur +=1
    
 
