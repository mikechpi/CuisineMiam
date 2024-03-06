from nutrition_api import get_nutritional_value_by_ingredients


def test_get_nutritional_value():

    # Demander à l'utilisateur de saisir l'ingrédient
    ingredient = input("Rentrez l'ingrédiant choisi : ")

    # Test avec l'ingrédient saisi
    print("Test avec l'ingrédient saisi :", ingredient)
    result = get_nutritional_value_by_ingredients([ingredient])
    if result is not None:
        print("Résultat du test avec l'ingrédient saisi :", result)
    else:
        print("Échec du test avec l'ingrédient saisi.")
    print()


if __name__ == "__main__":
    test_get_nutritional_value()
