age = int(input("Quel est ton age ? "))
if age >= 150:
    print("Tu es sûrement un highlander")
elif age >= 18:
    print("tu es majeur pour boire" )
elif 1 < age < 18: 
    print(f"{age} ans, mais tu es encore trop jeune pour boire, attend encore { 18 - age} ans pour être Majeur!")
elif age < 0:
    print("Menteur, tu ne serai pas encore né avec un tel age")
else :
    print("De l'alcool dans ton biberon?! HORS DE QUESTION.")

    # LE CODE DEMANDE L'AGE ET REPOND EN FONTION DE L'AGE DU CLIENT