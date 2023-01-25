import random

HERO = ENNEMY = 50
QUESTION = "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
REPONSE_CHOICES = ["1", "2"]
user_choice = ""

while True: 
    
    while user_choice not in REPONSE_CHOICES:
        user_choice = input(QUESTION)
        if user_choice not in REPONSE_CHOICES:
            print(f"Veuillez selectionner une des deux options valide")

    hero_attack = random.randint(5,10)
    ennemy_attack = random.randint(5,15)

    while not (HERO <= 0 or ENNEMY <= 0):
        user_choice = input(QUESTION)
        if user_choice == "1": 
            if (HERO > 0 or ENNEMY > 0):
                HERO = int(HERO) - int(ennemy_attack)
                ENNEMY = int(ENNEMY) - int(hero_attack)
                print(f"Vous avez infligé {hero_attack} de dommage HP")
                print(f"L'ennemi vous a infligé {ennemy_attack} de dommage HP")
                print(f"le hero à {HERO} de HP")
                print(f"l'ennemi à {ENNEMY} de HP")
                print(50 * "-")                
            else :
                print("FIN DU GAME")
                break

        elif user_choice == "2":
            potions_max = 3
            reste_potions = 1
            if potions_max > 0:
                reste_potions = potions_max - reste_potions 
                print(f"Vous venez d'utiliser une potion, il vous reste {reste_potions}")
                reste_potions +=1