import requests
from nutrition_api import get_nutritional_value_by_ingredients


def test_get_nutritional_value():

    # Test avec quelques ingrédients
    ingredients = ["apple", "banana", "orange"]
    print("Test avec quelques ingrédients :")
    result = get_nutritional_value_by_ingredients(ingredients)
    if result is not None:
        print("Résultat du test avec quelques ingrédients :", result)
    else:
        print("Échec du test avec quelques ingrédients.")
    print()

    # Test avec d'autres ingrédients
    ingredients = ["chicken breast", "rice", "broccoli"]
    print("Test avec d'autres ingrédients :")
    result = get_nutritional_value_by_ingredients(ingredients)
    if result is not None:
        print("Résultat du test avec d'autres ingrédients :", result)
    else:
        print("Échec du test avec d'autres ingrédients.")
    print()


if __name__ == "__main__":
    test_get_nutritional_value()
