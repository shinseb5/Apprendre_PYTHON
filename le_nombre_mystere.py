# LE NOMBRE MYSTERE

# - LE PROGRAMME CRÉE UN NOMBRE MYSTERE ALEATOIRE ET LE STOCK DANS UNE VARIABLE
# - LE PROGRAMME DOIT DEMANDER UN NOMBRE VALIDE ENTRE 0 ET 100
# - LE PROGRAMME VÉRIFIE SI LA VALEUR DONNER EST BIEN UN NOMBRE
# - APRES VALIDATION QU'IL S'AGIT BIEN D'UN NOMBRE : 
# - LE PROGRAMME ANNONCE LES REGLES ET NOMBRE D'ESSAIS = 5
# - LE PROGRAMME FAIT LA COMPARAISON ENTRE LE NOMBRE MYSTERE ET LE NOMBRE DONNER PAR LE CLIENT :
#       - SI IL EST INFERIEUR : ANNONCE QUE LE CHIFFRE MYSTERE EST PLUS PETIT QUE LA VALEUR DONNER PRECEDEMENT
#       - SI IL EST SUPERIEUR : ANNONCE QUE LE CHIFFRE MYSTERE EST PLUS GRAND QUE LA VALEUR DONNER PRECEDEMENT
# - SI IL EST EGAL : ANNONCE "BRAVO! LE NOMBRE MYSTERE ETAIT BIEN { LA VARIABLE ALÉATOIRE } ! " 
# - ET AFFICHE LE NOMBRE D'ESSAIS EFFECTUÉ
# - SI LE NOMBRE MYSTERE N'AS PAS ÉTÉ TROUVER ANNONCÉ "DOMMAGE, LE NOMBRE MYSTERE N'AS PAS ÉTÉ TROUVÉ"
# - LE PROGRAMME ANNONCE "FIN DU JEU."

# __________________________________________________________________________________________________________

# - IMPORTATION DE RANDOM POUR L'UTILISATION DE .randint()

import random

# - LE PROGRAMME CRÉE UN NOMBRE MYSTERE ALEATOIRE ET LE STOCK DANS UNE VARIABLE

MYSTERE_NUMBER_RANDOM = (random.randint(0, 100))
# print(MYSTERE_NUMBER_RANDOM)
# print("Le jeu du nombre mystère")

essais_total = 5 

while essais_total > 0:
    print(f"Il te reste {essais_total} éssais")
    demande_utilisateur =  input("A quel nombre pensez-vous? ")

    if not demande_utilisateur.isdigit():
        print("Veuillez entrer un nombre valide!")
        continue
    
    demande_utilisateur = int(demande_utilisateur)

    if demande_utilisateur > 100:
        print("Le nombre mystère se situe entre 0 et 100")
    elif demande_utilisateur > MYSTERE_NUMBER_RANDOM:
        print(f"Le nombre mystère est plus petit que {demande_utilisateur}")
        essais_total -= 1
        print(f"il reste {essais_total}  éssais")
    elif demande_utilisateur < MYSTERE_NUMBER_RANDOM:
        print(f"Le nombre mystère est plus grand que {demande_utilisateur}")
        essais_total -= 1
        print(f"il reste {essais_total} éssais")
    else :
        print(f"Bravo! {demande_utilisateur} est bien le chiffre mystère")
        print(f"Vous avez trouvé le nombre mystère en {6 - essais_total} éssais")
        break

if essais_total == 0:
    print(f"Vous n'avez pas trouvé le nombre mystère qui était {MYSTERE_NUMBER_RANDOM}")

print("FIN DU GAME")


# ______________________________________________________________________________________________

    # TANTQUE demande_utilisateur est un STRING alors : 
    #     FAIRE une vérification si la demande_utilisateurest dans la liste VALUES_LIST_CHOICES:
    #         SI demande_utilisateur > MYSTERE_NUMBER_RANDOM:
    #             ALORS ECRIRE (le nombre est plus petit)
    #             ECRIRE LE NOMBRE D'ÉSSAIS
    #         OU SI demande_utilisateur < MYSTERE_NUMBER_RANDOM:
    #             ALORS ECRIRE (le nombre est plus grand)
    #             ECRIRE LE NOMBRE D'ÉSSAIS
    #         OU SI demande_utilisateur == MYSTERE_NUMBER_RANDOM:
    #             ALORS ECRIRE (Bravo! vous avez trouver le nombre mystère en tant de NOMBRE D'ÉSSAIS)
    #             terminer le programme 
    #         OU SI NOMBRE D'ÉSSAIS = 0:
    #             ALORS ECRIRE (Désolé mais vous n'avez pas trouvé le nombre mystère)
    #             terminer le programme      
    

