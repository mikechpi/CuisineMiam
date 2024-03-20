import os
# La bibliothèque 'requests' permet de faire des requêtes HTTP depuis Python
import requests
# Chargement des variables d'environnement depuis un fichier .env
from dotenv import load_dotenv
load_dotenv()

API_ID = os.getenv("API_ID_FOOD_BIS")
API_KEY = os.getenv("API_KEY_FOOD_BIS")


def get_recipe_by_name(recipe_name):
    # La fonction get_recipe_by_name prend en entrée une
    # clé API et le nom d'une recette

    base_url = "https://api.edamam.com/api/recipes/v2?type=public"
    
    final_url = f"{base_url}&app_id={API_ID}&app_key={API_KEY}"

    params = {"q": recipe_name}

    response = requests.get(final_url, params=params)
    # envoie une requête GET à l'API Edamam avec les paramètres spécifiés,
    # et stocke la réponse dans une variable 'response'

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


# L'utilisateur va être invité à entrer le nom d'une recette.
# La fonction get_recipe_by_name est alors appelée avec la clé API
# et le nom de la recette. Si une recette correspondant au nom spécifié
# est trouvée, les informations de la recette sont affichées.
# Sinon, un message d'erreur est affiché.
api_key = "46df1aff8431edce2ce1f40a0b9bb08e"

if __name__ == '__main__':
    recipe_name = input("Quelle recette cherchez-vous ? ")
    recipe = get_recipe_by_name(recipe_name)
    if recipe:
        print(f"Nom de la recette: {recipe['label']}")
        print(f"Ingrédients: {recipe['ingredientLines']}")
