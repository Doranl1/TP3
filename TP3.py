"""
Exercice: TP3
Nom: Liam Doran
Group: 404
"""
import random
import time
# Les variables
force_adversaire = 0
numero_adversaire = 1
niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
jeu = True

while jeu:  # le début du jeu
    if nombre_victoires_consecutives == 3:
        force_adversaire = random.randint(4, 5) + random.randint(4, 5)
        print("Vous tombez face à face avec un boss de difficulté : %d"
              % force_adversaire)
    else:
        force_adversaire = random.randint(1, 5) + random.randint(1, 5)
        print("Vous tombez face à face avec un adversaire de difficulté : %d"
              % force_adversaire)
    choix = input("Que voulez-vous faire ? \n"
                  "1- Combattre cet adversaire\n"
                  "2- Contourner cet adversaire et aller ouvrir une autre porte\n"
                  "3- Afficher les règles du jeu\n"
                  "4- Quitter la partie\n")

    if int(choix) == 1:  # combattre l'adversaire
        print("Adversaire : %d\n"
              "Force de l’adversaire : %d\n"
              "Niveau de vie de l’usager : %d\n"
              "Combat %d : %d vs %d"
              % (numero_adversaire, force_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites))

        time.sleep(0.5)
        score_de = random.randint(1, 6) + random.randint(1, 6)
        print("Lancer du dé : %d"
              % score_de)
        time.sleep(1)

        if score_de <= force_adversaire:  # défaite du jouer
            niveau_vie -= force_adversaire

            if niveau_vie <= 0:  # la fin du partie
                print("La partie est terminée, vous avez vaincu %d monstre(s)."
                      % nombre_victoires)
                time.sleep(1)
                jouer = str(input("voulez-vous rejouer?\n"))

                if jouer == "oui":
                    print(" ")

                else:
                    jeu = False

            else:
                nombre_defaites += 1
                print("défaite\n"
                      "Niveau de vie : %d"
                      % niveau_vie)
                print(nombre_defaites)
                time.sleep(1)

        elif score_de > force_adversaire:  # victoire du joueur
            nombre_victoires += 1
            nombre_victoires_consecutives += 1
            niveau_vie += force_adversaire
            print("victoire\n"
                  "Niveau de vie : %d\n"
                  "Nombre de victoires consécutives : %d"
                  % (niveau_vie, nombre_victoires_consecutives))
            time.sleep(1)

    elif int(choix) == 2:  # contourner l'adversaire
        print("vous contournez cet adversaire et ouvre une autre porte")
        niveau_vie -= 1
        print("Niveau de vie : %d" % niveau_vie)
        time.sleep(3)

    elif int(choix) == 3:  # les règles
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  "
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
              "Une défaite a lieu lorsque la valeur du dé lancé "
              "par l’usager est inférieure ou égale à la force de l’adversaire.  "
              "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire, "
              "dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
        time.sleep(3)

    elif int(choix) == 4:  # quitter le jeu
        jouer = str(input("voulez-vous quitter?\n"))

        if jouer == "oui":
            jeu = False

        else:
            print("\n")
