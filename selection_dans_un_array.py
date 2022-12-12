# CREATION D'UNE LISTE
nombre_list = list(range(-10, 15))
print(nombre_list)

# FORME RACCOURCI D'UNE BOUCLE FOR AVEC UNE CONDITION SUR UNE RECHERCHE FILTRÉ DE NOMBRE DANS UNE VARIABLE DE TYPE ARRAY
# AVEC MULTIPLICATION
nombre_list_negatif = [i * 2 for i in nombre_list if i <= 0]
nombre_list_positif = [i * 3 for i in nombre_list if i > 0]

print(nombre_list_negatif)
print(nombre_list_positif)

# FORME RACCOURCI D'UNE BOUCLE FOR AVEC UNE CONDITION SUR UNE RECHERCHE FILTRÉ DE NOMBRE DANS UNE VARIABLE DE TYPE ARRAY
# SANS MULTIPLICATION
nombre_list_negatif = [i for i in nombre_list if i <= 0]
nombre_list_positif = [i for i in nombre_list if i > 0]

print(nombre_list_negatif)
print(nombre_list_positif)