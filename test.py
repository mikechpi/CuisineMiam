import requests

def get_recipes(api_key, ingredients):
    #base_url = "https://api.spoonacular.com/food/products/search?query=yogurt&apiKey=e6c29705f9a846f281775fb354ea534c"
    base_url = "https://api.edamam.com/api/recipes/v2?type=public&q=eggs%2C%20milk&app_id=8a33a29b&app_key=5c0e46d6a1d3106ff55a5e2925e27f76"
    #base_url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        'q': ','.join(ingredients),
        'app_id': '8a33a29b', 
        'app_key' : '5c0e46d6a1d3106ff55a5e2925e27f76'
        #'app_key' : 'e6c29705f9a846f281775fb354ea534c'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("test")
        return data.get('hits', [])
    else:
        print(f"Erreur lors de la requête à l'API: {response.status_code}")
        return []

# Exemple d'utilisation
ingredients = ["lait", "farine", "oeuf"]
# api_key = "e6c29705f9a846f281775fb354ea534c"
api_key = "5c0e46d6a1d3106ff55a5e2925e27f76"
recipes = get_recipes(api_key, ingredients)

for recipe in recipes:
    print(f"Nom de la recette: {recipe['recipe']['label']}")
    # print(f"Ingrédients: {recipe['recipe']['ingredientLines']}")
    print("-----")
