from nutrition_api import get_nutritional_value_by_ingredients


def test_get_nutritional_value():
    # Définir l'ingrédient choisi comme le steak
    ingredient = "steak"

    # Afficher l'ingrédient choisi
    print("Ingrédient choisi :", ingredient)

    # Obtenir la valeur nutritionnelle de l'ingrédient
    result = get_nutritional_value_by_ingredients([ingredient])

    # Afficher le résultat
    if result is not None:
        print("Résultat de la valeur nutritionnelle :", result)
    else:
        print("Échec de l'obtention de la valeur nutritionnelle.")

    print()


if __name__ == "__main__":
    test_get_nutritional_value()
