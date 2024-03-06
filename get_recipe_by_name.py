import requests
# La bibliothèque 'requests' permet de faire des requêtes HTTP depuis Python


# Chargement des variables d'environnement depuis un fichier .env
from dotenv import load_dotenv
load_dotenv()


def get_recipe_by_name(api_key, recipe_name):
    # La fonction get_recipe_by_name prend en entrée une
    # clé API et le nom d'une recette
    base_url = (
        "https://api.edamam.com/api/recipes/v2"
        "?type=public&app_id=9c60bb8a&app_key=46df1aff8431edce2ce1f40a0b9bb08e"
    )
    # base_url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {"q": recipe_name}

    response = requests.get(base_url, params=params)
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
    recipe = get_recipe_by_name(api_key, recipe_name)
    if recipe:
        print(f"Nom de la recette: {recipe['label']}")
        print(f"Ingrédients: {recipe['ingredientLines']}")
        print(f"Instructions: {recipe['url']}")
