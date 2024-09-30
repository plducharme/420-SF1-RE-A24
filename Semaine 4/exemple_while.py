termine = False
total = 0
while not termine:
    nombre = input("Entrer un nombre ou fin pour terminer: ")

    if nombre == 'fin':
        termine = True
        print("Total:\t" + str(total))
        # break arrête l'exécution de l'itération courante pour passer à la prochaine itération
        break
    else:
        total += int(nombre)
    print("Ceci est exécuté, mais pas s'il y a un break")

