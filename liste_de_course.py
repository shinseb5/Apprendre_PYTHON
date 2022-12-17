demande_client ="0"
liste_de_course = []

while demande_client.isdigit():

    print ("""_______________________________________________________
    Choisissez parmi les 5 options suivantes :
    1 : Ajouter un élément à la liste
    2 : Retirer un élément de la liste
    3 : Afficher la liste
    4 : Vider la liste
    5 : Quitter""")
    demande_client = input("Votre choix : ")    
    
    if demande_client < "1" :
        print("nombre non valide!")
    elif demande_client >= "6":
        print("La demande n'est pas dans la liste")
    elif demande_client == "1" :
        nouveau_element = input("Que voulez-vous rajouter à la liste de course ? ")
        liste_de_course.append(nouveau_element)
        continue
    elif demande_client == "2" :
        retirer_element = input("Quel élément est à retirer ? ")
        liste_de_course.remove(retirer_element)
        continue
    elif demande_client == "3" :
        print(liste_de_course)
        continue
    elif demande_client == "4" :
        liste_de_course.clear()
        continue
    elif demande_client == "5" :
        print("À bientôt!")
        break