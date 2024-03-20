
from get_recipe_by_name import get_recipe_by_name


def test_get_recipe_by_name():
    api_key = "46df1aff8431edce2ce1f40a0b9bb08e"
    recipes_to_test = [
        ("pizza", {"label": "Pizza Dough"}),
        ("salade", {"label": "Salade Indochinoise"}),
        ("tarte", {"label": "Tarte Tatin"}),
        ("pâtes", {"label": "(Very) Peppery Pate"}),
        ("recette inexistante", None)
    ]

    for recipe_name, expected_result in recipes_to_test:
        result = get_recipe_by_name(api_key, recipe_name)

        if expected_result is None:
            assert result is None, (
                f"La recette '{recipe_name}' devrait renvoyer None")
        else:
            assert result is not None, (
                f"La recette '{recipe_name}' ne devrait pas renvoyer None")
            assert result['label'] == expected_result['label'], (
                f"Le nom de la recette '{recipe_name}' ne correspond pas")
