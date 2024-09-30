marque = input("Quel est la marque de votre scie à chaîne? ")

match marque:
    # Va faire un "match" sur un des "case".
    case "Husqvarna":
        print("La fiabilité nordique")
    case "Stihl":
        print("C'est du solide")
    case "Yardworks":
        print("Bon rapport qualité-prix")
    # Aucun "match", le cas par défaut
    case _:
        print("Je ne connais pas la marque!")

