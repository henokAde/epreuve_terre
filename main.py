import math

# ALPHABET
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for lettre in alphabet:
    print(lettre)

# Nom du programme
chemin_complet = __file__
nom_fichier = chemin_complet.split('/')[-1]
print(nom_fichier)


# Afficheur d’arguments
arguments = input("Entrez les arguments (séparés par des espaces) : ").split()

for argument in arguments:
    print(argument)


# L’alphabet à partir de
def afficher_alphabet(lettre_debut):
    if lettre_debut in alphabet:
        index_debut = alphabet.index(lettre_debut)
        for lettre in alphabet[index_debut:]:
            print(lettre)
    else:
        print("Veuillez entrer une lettre minuscule valide.")

afficher_alphabet("y")


# Pair ou impair
def est_pair_impair(nombre):
    if nombre % 2 == 0:
       print(f"{nombre} est un entier pair.")
    else:
        print(f"{nombre} est un entier impair.")

est_pair_impair(5)


# Divisions
def division_et_reste(dividende, diviseur):
    resultat = dividende // diviseur
    reste = dividende % diviseur

    print(f"Résultat de la division : {resultat}")
    print(f"Reste de la division : {reste}")

division_et_reste(5,10)


# Inverser une chaîne
def afficher_inverse(chaine):
    inverse = chaine[::-1]
    print(inverse)

afficher_inverse('hello')


# Taille d’une chaîne
def afficher_nombre_caracteres(chaine):
    nombre_caracteres = len(chaine)
    print(f"La chaîne contient {nombre_caracteres} caractères.")
afficher_nombre_caracteres("Hello")


# Puissance d’un nombre
def calculer_puissance(base, exposant):
    if not (isinstance(base, (int, float)) and isinstance(exposant, int)):
        print("Les arguments doivent être des nombres.")

    if exposant < 0:
        print("L'exposant ne peut pas être négatif.")

    resultat = base ** exposant
    print(resultat)

calculer_puissance(10, 4)


# Racine carrée d’un nombre
def afficher_racine_carree(nombre):
    if isinstance(nombre, (int, float)):
        if nombre >= 0:
            racine = math.sqrt(nombre)
            print(f"La racine carrée de {nombre} est : {racine}")
        else:
            print("L'argument doit être un entier positif.")
    else:
        print("L'argument doit être un nombre.")


afficher_racine_carree(4)


# Nombre premier
def est_nombre_premier(nombre):
    if not isinstance(nombre, int) or nombre <= 1:
        print("Non, ce n'est pas un nombre premier.")
        return

    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            print("Non, ce n'est pas un nombre premier.")
            return
    print("Oui, c'est un nombre premier.")
est_nombre_premier(5)


# 24 to 12
def convertir_format_12h(heure_24h):
    try:
        heure, minute = map(int, heure_24h.split(':'))
    except ValueError:
        try:
            heure = int(heure_24h)
            minute = 0
        except ValueError:
            print("Format d'heure invalide.")
            return

    if 0 <= heure < 24 and 0 <= minute < 60:
        if heure == 0:
            heure_12h = 12
            suffixe = "AM"
        elif heure == 12:
            heure_12h = 12
            suffixe = "PM"
        elif heure < 12:
            heure_12h = heure
            suffixe = "AM"
        else:
            heure_12h = heure - 12
            suffixe = "PM"

        heure_12h_str = f"{heure_12h:02d}:{minute:02d}{suffixe}"
        print(heure_12h_str)
    else:
        print("Format d'heure invalide.")


convertir_format_12h("20:40")

# 12 to 24

def convertir_format_24h(heure_12h):
    heure_12h = heure_12h.upper()

    try:
        heure, minute = map(int, heure_12h[:-2].split(':'))
    except ValueError:
        print("Format d'heure invalide.")
        return

    suffixe = heure_12h[-2:]
    if suffixe == "AM":
        if heure == 12:
            heure_24h = 0
        else:
            heure_24h = heure
    elif suffixe == "PM":
        if heure == 12:
            heure_24h = 12
        else:
            heure_24h = heure + 12
    else:
        print("Suffixe AM/PM invalide.")
        return

    if 0 <= heure_24h <= 23 and 0 <= minute <= 59:
        heure_24h_str = f"{heure_24h:02d}:{minute:02d}"
        print(heure_24h_str)
    else:
        print("Format d'heure invalide.")

convertir_format_24h("11:09PM")


# Trouver la Suisse
def trouver_valeur_milieu(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        print("Problème : les arguments doivent être des nombres.")
    elif a == b == c:
        print("erreur.")
    else:
        min_val = min(a, b, c)
        max_val = max(a, b, c)
        milieu_val = a + b + c - min_val - max_val
        print(milieu_val)

trouver_valeur_milieu(10, 20, 30)

# Trié ou pas
def est_triee(liste):
    if not all(isinstance(item, (int, float)) for item in liste):
        print("Problème : les éléments de la liste doivent être des nombres.")
        return

    triee = True
    for i in range(1, len(liste)):
        if liste[i] < liste[i - 1]:
            triee = False
            break

    if triee:
        print("Triée !")
    else:
        print("Pas triée !")


est_triee([1,2,3])


# Terre : ok
def celebrer_victoire(adjectif):
    message = f"J’ai terminé l’Épreuve de la Terre et c’était {adjectif}."
    print(message)

celebrer_victoire("easy lol")






