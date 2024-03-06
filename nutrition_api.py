import requests
from dotenv import load_dotenv
import os


def get_nutritional_value_by_ingredients(ingredients):
    # Charger les informations d'identification depuis le fichier .env
    load_dotenv()

    # Base URL de l'API Edamam
    base_url = "https://api.edamam.com/api/nutrition-details"

    # Paramètres de l'API Edamam (app_id et app_key)
    app_id = os.getenv("APP_ID")
    app_key = os.getenv("APP_KEY")

    # Vérifier que les clés d'API ont été chargées correctement
    if not app_id or not app_key:
        print("Erreur: Les clés d'API Edamam n'ont pas été chargées.")
        return None

    # Construire l'URL de requête
    params = {
        "app_id": app_id,
        "app_key": app_key,
    }
    data = {
        "ingredients": [
            {
                "quantity": 1,
                "measureURI": "",
                "foodId": ingredient
            }
            for ingredient in ingredients
        ]
    }

    try:
        print("Envoi de la requête à l'API Edamam...")
        response = requests.post(base_url, params=params, json=data)
        # Lèvera une exception si le code de statut HTTP n'est pas 2xx
        response.raise_for_status()
        print("Réponse reçue avec succès de l'API Edamam.")
    except requests.exceptions.HTTPError as err:
        print(f"Erreur HTTP lors de la requête à l'API Edamam: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Une erreur lors de la requête à l'API Edamam: {err}")
        return None

    # Traiter la réponse et retourner les données nutritionnelles
    if response.status_code == 200:
        nutrition_data = response.json()
        nutritional_values = {}
        for ingredient_data in nutrition_data.get("ingredients", []):
            parsed_data = ingredient_data.get("parsed", {})
            food_data = parsed_data.get("food", {})
            ingredient_name = food_data.get("label")

            if ingredient_name:
                nutritional_values[ingredient_name] = {}
                parsed_data = ingredient_data.get("parsed", {})
                nutrients_data = parsed_data.get("nutrients", [])
                for nutrient in nutrients_data:
                    nutrient_label = nutrient["label"]
                    nutrient_quantity = nutrient["quantity"]
                    nutritional_values[ingredient_name][nutrient_label] = \
                        nutrient_quantity
        return nutritional_values
    else:
        print(f"Erreur lors de la récupération des valeurs nutritionnelles. "
        f"Code de statut: {response.status_code}")
        return None
