# Pour chaque élément de l'argument liste :
# - si le nombre de caractère vaut 1 : ajoute le caractère '0' devant la valeur
# - sinon ne fait rien
# Renvoie ensuite la liste modifiée
def r(liste):
    for i in range (len(liste)):
        if len(liste[i]) == 1:
            (liste[i]) = "0"+ (liste[i])
    return liste
    
