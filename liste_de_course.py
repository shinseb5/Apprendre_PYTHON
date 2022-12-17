# Initialisations des variables
demande_client ="0"
liste_de_course = []

# Démarrage de la boucle While
while demande_client.isdigit():
    print("_" * 70)
    print ("""Choisissez parmi les 5 options suivantes :
    1 : Ajouter un élément à la liste
    2 : Retirer un élément de la liste
    3 : Afficher la liste
    4 : Vider la liste
    5 : Quitter""")
    demande_client = input("Votre choix : ")    
# vérification si le nombre est correcte    
    if demande_client < "1" :
        print("nombre non valide!")
    elif demande_client >= "6":
        print("La demande n'est pas dans la liste")
# Ajouter un élément
    elif demande_client == "1" :
        nouveau_element = input("Que voulez-vous rajouter à la liste de course ? ")
        liste_de_course.append(nouveau_element)
# Enlever un élément
    elif demande_client == "2" : 
        retirer_element = input("Quel élément est à retirer ? ")
        if retirer_element in liste_de_course :           
            liste_de_course.remove(retirer_element)
        else :
            print("cette article n'est pas dans la liste de course")
# Voir la liste 
    elif demande_client == "3" : 
        if not liste_de_course == []:
            print("Voici votre liste de course : ")
            for i in liste_de_course :
                modif_index_liste_de_course = liste_de_course.index(i)
                modif_index_liste_de_course +=1
                print(f"{modif_index_liste_de_course}. {i}")
        else :
            print("Votre liste de course est vide!")
# Vider la liste
    elif demande_client == "4" :
        liste_de_course.clear()
        print("La liste de course a été vidée de son contenu.")
# Sortir du Script
    elif demande_client == "5" :
        print("À bientôt!")
        break