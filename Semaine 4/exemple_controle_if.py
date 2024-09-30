# On demande à l'utilisateur d'entrer son âge
age = input("Quel est votre âge? ")
# Vérifie si la valeur entrée est un nombre
if age.isnumeric():
    # Transforme la str en int
    age = int(age)
    # première condition évaluée
    if age >= 18:
        print("Vous êtes majeur, mais êtes vous sage?")
    # Si la première condition n'est pas vraie, celle-ci sera évaluée
    elif age < 3:
        print("Areuh" * 3)
    # Aucun autre condition n'est vraie, ce bloc d'instructions sera exécuté
    else:
        print("Ça grandit vite!")
else:
    print(f"L'âge entré <{age}> n'est pas valide")

