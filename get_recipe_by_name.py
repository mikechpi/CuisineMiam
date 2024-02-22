import requests
#La bibliothèque 'requests' permet de faire des requêtes HTTP depuis Python


from dotenv import load_dotenv
load_dotenv()


def get_recipe_by_name(api_key, recipe_name): #La fonction get_recipe_by_name prend en entrée une clé API et le nom d'une recette
    base_url = "https://api.edamam.com/api/recipes/v2?type=public&app_id=9c60bb8a&app_key=46df1aff8431edce2ce1f40a0b9bb08e&q=chiken"
    #base_url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        'q': recipe_name,
        'type': 'public',
        'app_id': '9c60bb8a',
        'app_key': '46df1aff8431edce2ce1f40a0b9bb08e',
        'random': 'true'
    }

    response = requests.get(base_url, params=params) 
    #envoie une requête GET à l'API Edamam avec les paramètres spécifiés, et stocke la réponse dans une variable 'response'

    if response.status_code == 200:
        data = response.json()
        if data['hits']:
            return data['hits'][0]['recipe']
        else:
            print("Aucune recette trouvée pour ce nom.")
            return None
    else:
        print(f"Erreur lors de la requête à l'API: {response.status_code}")
        return None

# Exemple d'utilisation
ingredient = ["poulet", "oignon"]
api_key = "46df1aff8431edce2ce1f40a0b9bb08e"
# api_key = "46df1aff8431edce2ce1f40a0b9bb08e"
recipe_name = "tarte aux pommes"
recipe = get_recipe_by_name(api_key, recipe_name)

if recipe:
    print(f"Nom de la recette: {recipe['label']}")
    print(f"Ingrédients: {recipe['ingredientLines']}")
    print(f"Instructions: {recipe['url']}")