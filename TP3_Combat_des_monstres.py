"""
Tp3 Combat de monstre
par camille voisin 404 le 9 septembre 2025
"""

import random as rd


PV = 20
force_monstre = rd.randint(1, 5)
lancer_player = rd.randint(1, 6)
suite_de_monstres_tues = 0
nb_defaite = 0
nb_victoire = 0
nb_monstre_combattus = nb_victoire + nb_defaite
nb_monstres_rencontres = nb_victoire + nb_defaite
while PV != 0:
    print("Note du développeur : il est préférable d'agrandir le terminal "
          "le plus possible pour une meilleure expérience")
    menu_debut_jeu = str(input("Que voulez vous faire?\n1- Lancer le jeu?\n2- Lire les règles?\n"))
    if menu_debut_jeu == "1":
        while PV != 0:
            force_monstre = rd.randint(1, 5)
            print(f"Vous combattez contre votre {nb_monstre_combattus + 1}e monstre et vous rencontrez votre"
                  f" {nb_monstres_rencontres + 1}e monstre.")
            print(f"La dificulté du prochain monstre est : {force_monstre}.")
            menu = str(input("Que voulez vous faire? \n1- Faire mon combat "
                             "\n2- Skipper mon combat et perdre un PV \n3- Quitter la partie \n"))
            if menu == "1":
                nb_monstre_combattus += 1
                nb_monstres_rencontres += 1
                lancer_player = rd.randint(1, 6)
                print("Vous affrontez le monstre.")
                print(f"Votre force est de : {lancer_player}.")
                if lancer_player < force_monstre:
                    print(f"Vous perdez votre combat et perdez {force_monstre} PV")
                    PV = PV - force_monstre
                    nb_defaite += 1
                    suite_de_monstres_tues = 0
                    print(f"Vous avez maintenant {PV} PV.\nVotre kill streak est maintenant {suite_de_monstres_tues} "
                          f"et vous avez {nb_defaite} défaites et {nb_victoire} victoires ")

                elif lancer_player >= force_monstre:
                    nb_victoire += 1
                    force_monstre = rd.randint(1, 5)
                    suite_de_monstres_tues = suite_de_monstres_tues + 1
                    PV += force_monstre
                    print(f"Vous avez gagné {force_monstre} PV, vous avez maintenant {PV} PV")
            elif menu == "2":
                nb_monstres_rencontres += 1
                PV = PV - 1
                print(f"\nVous fuyez votre combat comme un lâche et perdez un PV. \nVous avez maintenant {PV} PV")
                print(f"Votre kill streak est de {suite_de_monstres_tues * 0} et"
                      f" vous avez {nb_victoire} victoires et {nb_defaite} défaites.\n")
            elif menu == "3":
                print("Vous quittez le jeu.")
                exit()
    elif menu_debut_jeu == "2":
        print("Les règels sont simples,"
              " vous lancez un dé et regardez si vous avez un score supérieur à celui du monstre."
              "\nSi oui, vous gagnez sa force en PV, si non, vous perdez sa force en PV.\n"
              "Lorsque vous gagnez, votre kill streak augmente et vous gagnez votre score d'une victoire, "
              "si vous perdez, votre streak se reset et vous avez un defaite.\n")
