import requests
import os
from dotenv import load_dotenv
load_dotenv()

URL = "https://api.edamam.com/api/recipes/v2?type=public"
KEY = os.getenv("API_KEY_FOOD")
ID = os.getenv("API_ID_FOOD")


def getNameRecipesByNameIngredients(ingredients):

    base_url = URL
    app_id = ID
    app_key = KEY

    final_url = f"{base_url}&q={ingredients}&app_id={app_id}&app_key={app_key}"
    print("final_url: ", final_url)

    response = requests.get(final_url)

    if response.status_code == 200:
        data = response.json()
        return data.get('hits', [])
    else:
        print(f"Erreur lors de la requête à l'API: {response.status_code}")
        return []

# user_input = input("Enter ingredients: ")
# ingredients = [ingredient.strip() for ingredient in user_input.split(',')]

# recipes = getNameRecipesByNameIngredients(ingredients)


if __name__ == '__main__':
    user_input = input("Enter ingredients: ")
    ingredients = [ingredient.strip() for ingredient in user_input.split(',')]
    recipes = getNameRecipesByNameIngredients(ingredients)
    for recipe in recipes:
        print(f"Name of the recipes : {recipe['recipe']['label']}")
        print(f"Ingredients: {recipe['recipe']['ingredientLines']}")
        print("-----")
