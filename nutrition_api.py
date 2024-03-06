import requests
from dotenv import load_dotenv
import os


def get_nutritional_value_by_ingredients(ingredient):
    # Charger les informations d'identification depuis le fichier .env
    load_dotenv()

    # Base URL de l'API Edamam
    base_url = "https://api.edamam.com/api/nutrition-data"

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
        "nutrition-type": "logging",
        "ingr": ingredient
    }

    try:
        print("Envoi de la requête à l'API Edamam...")
        response = requests.get(base_url, params=params)
        # Lèvera une exception si le code de statut HTTP n'est pas 2xx
        response.raise_for_status()
        print("Réponse reçue avec succès de l'API Edamam.")
    except requests.exceptions.HTTPError as err:
        print(f"Erreur HTTP lors de la requête à l'API Edamam: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Une erreur lors de la requête à l'API Edamam: {err}")
        return None

    # Traiter la réponse et retourner les données nutritionnelles spécifiques
    if response.status_code == 200:
        nutrition_data = response.json()
        # Extraire les données spécifiques
        diet_labels = nutrition_data.get('dietLabels', [])
        co2_emissions_class = nutrition_data.get('co2EmissionsClass', "")
        calories = nutrition_data.get('calories', "")
        # Afficher un message en fonction de la classe d'émissions de CO2
        if co2_emissions_class == 'G':
            print("Attention: Cet aliment n'est pas bon pour la santé.")
        elif co2_emissions_class == 'A':
            print("Bon pour le corps et la planète: Cet aliment est good.")
        else:
            print("Classe d'émissions de CO2 inconnue.")
        return {
            'dietLabels': diet_labels,
            'co2EmissionsClass': co2_emissions_class,
            'calories': calories
        }
    else:
        print(f"Erreur lors de la récupération des valeurs nutritionnelles. "
              f"Code de statut: {response.status_code}")
        return None
