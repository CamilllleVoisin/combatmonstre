"""
Tp3 Combat de monstre
par camille voisin 404 le 9 septembre 2025
"""

import random as rd


pv = 20
combat_boss = False
force_monstre = rd.randint(1, 5) + rd.randint(0, 5)
lancer_player = rd.randint(1, 6) + rd.randint(0, 6)
suite_de_monstres_tues = 0
nb_defaite = 0
nb_victoire = 0
nb_monstre_combattus = nb_victoire + nb_defaite
nb_monstres_rencontres = nb_victoire + nb_defaite
boss_rencontre = 0
skipped_combats = 0
while pv > 0:

    print(f"Vous combattez contre votre {nb_monstre_combattus + 1}e monstre et vous rencontrez votre"
          f" {nb_monstres_rencontres + 1}e monstre.")
    print(f"La dificulté du prochain monstre est : {force_monstre}.")
    menu = input("Que voulez vous faire? \n1- Faire mon combat "
                 "\n2- Contourner le monstre, et passer au prochain monstre et perdre un PV "
                 "\n3- Afficher les règles "
                 "\n4- Quitter la partie \n")

    if menu == "1":
        nb_monstre_combattus += 1
        nb_monstres_rencontres += 1
        lancer_player = rd.randint(1, 6) + rd.randint(0, 6)
        print("\nVous affrontez le monstre.")
        print(f"Votre force est de : {lancer_player}.")

        if lancer_player < force_monstre:
            print(f"Vous perdez votre combat et perdez {force_monstre} PV")
            pv -= force_monstre
            nb_defaite += 1
            suite_de_monstres_tues = 0
            print(f"Vous avez maintenant {pv} PV."
                  f"\nVotre kill streak est maintenant {suite_de_monstres_tues} "
                  f"et vous avez {nb_defaite} défaites et {nb_victoire} victoires et "
                  f"vous avez skippé {skipped_combats} combats ")
            force_monstre = rd.randint(1, 5) + rd.randint(0, 5)
            combat_boss = False

        elif lancer_player >= force_monstre:
            combat_boss = False
            nb_victoire += 1
            pv += force_monstre
            suite_de_monstres_tues += 1
            print(f"Vous avez gagné {force_monstre} PV, vous avez maintenant {pv} PV")
            print(f"Votre kill streak est de {suite_de_monstres_tues} et"
                  f" vous avez {nb_victoire} victoires et {nb_defaite} défaites et "
                  f"vous avez skippé {skipped_combats} combats.\n")
            force_monstre = rd.randint(1, 5) + rd.randint(0, 5)
            if suite_de_monstres_tues % 3 == 0:
                force_monstre = rd.randint(5, 7) + rd.randint(5, 7)
                print("\nAttention! Vous allez affronter un boss! Vous n'avez PAS le droit de skipper!")
                combat_boss = True

    elif menu == "2":
        if combat_boss is True:
            print("\nOh la la! Vous avez essayé de fuir le boss, mais le voilà qui s'interpose ente la porte et vous!"
                  " Vous pensiez faire quoi?? :p")

        else:
            force_monstre = rd.randint(1, 5) + rd.randint(0, 5)
            nb_monstres_rencontres += 1
            pv -= 1
            suite_de_monstres_tues = 0
            skipped_combats += 1
            print(f"\nVous fuyez votre combat comme un lâche et perdez un PV. \nVous avez maintenant {pv} PV")
            print(f"Votre kill streak est de {suite_de_monstres_tues} et"
                  f" vous avez {nb_victoire} victoires et {nb_defaite} défaites et "
                  f"vous avez skippé {skipped_combats}combats.\n")

    elif menu == "3":
        print("Les règels sont simples,"
              " vous lancez un dé et regardez si vous avez un score supérieur à celui du monstre."
              "\nSi oui, vous gagnez sa force en PV, si non, vous perdez sa force en PV.\n"
              "Lorsque vous gagnez, votre kill streak augmente et vous gagnez votre score d'une victoire, "
              "si vous perdez, votre streak se reset et vous avez un defaite.\n")
        force_monstre = force_monstre

    elif menu == "4":
        print("Vous quittez le jeu.")
        exit()
if pv <= 0:
    print("Vous êtes morts, redémarrez le programme pour jouer a nouveau.")
