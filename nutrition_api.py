import requests
from dotenv import load_dotenv
import os

api_id = os.getenv("API_ID_NUTRITION_BIS")
api_key = os.getenv("API_KEY_NUTRITION_BIS")

class NutritionAPI:
    @staticmethod
    def get_nutritional_value_by_ingredients(ingredient):
        load_dotenv()

        base_url = "https://api.edamam.com/api/nutrition-data"

        if not api_id or not api_key:
            print("Erreur: Les clés d'API Edamam n'ont pas été chargées.")
            return None


        first_url = f"{base_url}&app_id={api_id}&app_key={api_key}"

        second_url = f"&ingr={ingredient}&nutrition-type=logging"

        final_url = first_url + second_url

        try:
            print("Envoi de la requête à l'API Edamam...")
            response = requests.get(final_url)
            # response.raise_for_status()
            print("Réponse reçue avec succès de l'API Edamam.")
        except requests.exceptions.HTTPError as err:
            print(f"Erreur HTTP lors de la requête à l'API Edamam: {err}")
            return None
        except requests.exceptions.RequestException as err:
            print(f"Une erreur lors de la requête à l'API Edamam: {err}")
            return None

        if response.status_code == 200:
            nutrition_data = response.json()
            diet_labels = nutrition_data.get('dietLabels', [])
            co2_emissions_class = nutrition_data.get('co2EmissionsClass', "")
            calories = nutrition_data.get('calories', "")

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
            print(f"Erreur lors de la récup des valeurs nutritionnelles. "
                  f"Code de statut: {response.status_code}")
            return None


if __name__ == "__main__":
    ingredient = input("Entrez un ingrédient : ")
    result = NutritionAPI.get_nutritional_value_by_ingredients(ingredient)
    print(result)
