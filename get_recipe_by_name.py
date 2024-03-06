import os
import requests

from dotenv import load_dotenv
load_dotenv()

API_ID = os.getenv("API_ID_FOOD_BIS")
API_KEY = os.getenv("API_KEY_FOOD_BIS")


def get_recipe_by_name(recipe_name):

    base_url = "https://api.edamam.com/api/recipes/v2?type=public"

    final_url = f"{base_url}&q={recipe_name}&app_id={API_ID}&app_key={API_KEY}"

    response = requests.get(final_url)


    if response.status_code == 200:
        data = response.json()
        return data.get('hits', [])
    else:
        print(f"Erreur lors de la requête à l'API: {response.status_code}")
        return []


if __name__ == '__main__':
    recipe_name = input("Quelle recette cherchez-vous ? ")
    recipes = get_recipe_by_name(recipe_name)
    for recipe in recipes:
        print(f"Nom de la recette: {recipe['recipe']['label']}")
        print(f"Ingrédients: {recipe['recipe']['ingredientLines']}")
