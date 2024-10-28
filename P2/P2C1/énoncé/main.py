def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    nombre_a_gauche = int(input("entrer un nombre"))
    nombre_a_droite = int(input("entrer un nombre"))
    opération = input("entrer une symbole d'opération (+, -, * ou /):") 
    resultat=0
    if nombre_a_gauche.isnumeric():
        print("numeric")
    else:
        print("Erreur: les deux nombres doivent être des nombres entiers")

    if nombre_a_droite.isnumeric():
        print("numeric")
    else:
        print("Erreur: les deux nombres doivent être des nombres entiers")
    match opération: 
        case"+":
            resultat = nombre_a_gauche + nombre_a_droite
        case"-":
            resultat = nombre_a_gauche-nombre_a_droite
        case"*":
            resultat=nombre_a_gauche*nombre_a_droite
        case"/":
            if nombre_a_droite==0:
                print("Erreur: impossible de diviser par zéro.")
            else:
               resultat=nombre_a_gauche/nombre_a_droite 
        case _:
            print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
