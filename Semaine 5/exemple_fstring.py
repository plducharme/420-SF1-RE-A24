# Les format string ou fstring permettent le formatage et la substitution de valeurs dans une string
prenom = "Pier Luc"
nom = "Ducharme"
# pour utiliser une fstring, précéder votre string avec "f"
print(f"Mon nom est {prenom} {nom}")
# Équivalent avec format
print("Mon nom est {prenom} {nom}".format(prenom=prenom, nom=nom))


# un des avantages est qu'il n'est pas nécessaire de "caster" (transtyper) un nombre avant de l'utiliser comme substitution
taille = 1.89
print(f"La grandeur est {taille}")
# code équivalent
print("La grandeur est " + str(taille))



