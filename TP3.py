import random
force_adversaire = random.randint(1, 5)
numero_adversaire = 1
niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
print("Vous tombez face à face avec un adversaire de difficulté : %d"
      %(force_adversaire))
choix = input("Que voulez-vous faire ? \n"
              "1- Combattre cet adversaire\n"
              "2- Contourner cet adversaire et aller ouvrir une autre porte\n"
              "3- Afficher les règles du jeu\n"
              "4- Quitter la partie\n")
if int(choix) == 1:
    numero_combat += 1
    print("Adversaire : %d\n"
    "Force de l’adversaire : %d\n"
    "Niveau de vie de l’usager : %d\n"
    "Combat %d : %d vs %d\n"
    %(numero_adversaire, force_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites))
    score_dé = random.randint(1, 6)
    print("Lancer du dé : %d"
          %(score_dé))
    if score_dé <= force_adversaire:
        niveau_vie -= force_adversaire
        if niveau_vie <= 0:
            print("La partie est terminée, vous avez vaincu %d monstre(s)."
                  %(nombre_victoires))
            break
        else:
            print("défaite\n"
                  "Niveau de vie : %d"
                  %(niveau_vie))
    elif score_dé > force_adversaire:
        nombre_victoires_consecutives += 1
        niveau_vie += force_adversaire
        print("victoire\n"
              "Niveau de vie : %d\n"
              "Nombre de victoires consécutives : %d"
              %(niveau_vie, nombre_victoires_consecutives))
