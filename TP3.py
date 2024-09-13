import random
force_adversaire = 0
numero_adversaire = 1
niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
jeu = 1
while jeu == 1:
    force_adversaire = random.randint(1, 5)
    print("Vous tombez face à face avec un adversaire de difficulté : %d"
          %(force_adversaire))
    choix = input("Que voulez-vous faire ? \n"
                  "1- Combattre cet adversaire\n"
                  "2- Contourner cet adversaire et aller ouvrir une autre porte\n"
                  "3- Afficher les règles du jeu\n"
                  "4- Quitter la partie\n")

    if int(choix) == 1:
        print("Adversaire : %d\n"
              "Force de l’adversaire : %d\n"
              "Niveau de vie de l’usager : %d\n"
              "Combat %d : %d vs %d"
              %(numero_adversaire, force_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites))
        score_dé = random.randint(1, 6)
        print("Lancer du dé : %d"
              %(score_dé))
        if score_dé <= force_adversaire:
            niveau_vie -= force_adversaire
            if niveau_vie <= 0:
                print("La partie est terminée, vous avez vaincu %d monstre(s)."
                      %(nombre_victoires))
                jouer = str(input("voulez-vous rejouer?\n"))
                if jouer == "oui":
                    print(" ")
                else:
                    break
            else:
                nombre_defaites += 1
                print("défaite\n"
                      "Niveau de vie : %d"
                      %(niveau_vie))
                print(nombre_defaites)
        elif score_dé > force_adversaire:
            nombre_victoires += 1
            nombre_victoires_consecutives += 1
            niveau_vie += force_adversaire
            print("victoire\n"
                  "Niveau de vie : %d\n"
                  "Nombre de victoires consécutives : %d"
                  %(niveau_vie, nombre_victoires_consecutives))
    elif int(choix) == 2:
        print("vous contournez cet adversaire et ouvre une autre porte")
    elif int(choix) == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
    elif int(choix) == 4:
        jouer = str(input("voulez-vous quitter?\n"))
        if jouer == "oui":
            break
        else:
            print(" ")