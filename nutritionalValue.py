import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_ID = os.getenv("API_ID_NUTRITION")
API_KEY = os.getenv("API_KEY_NUTRITION")


# Récupérer les valeurs nutritionnelles des plats en donnant un ingrédient
def get_nutritional_value_by_ingredients():
    base_url = "https://api.edamam.com/api/food-database/v2/parser?"

    ingredient = input("Enter an ingredient: ")
    ingredients_param = ingredient

    final_url = f"{base_url}&app_id={API_ID}&app_key={API_KEY}&ingr={ingredients_param}&nutrition-type=cooking"

    response = requests.get(final_url)

    if response.status_code == 200:
        data = response.json()
        return data.get('hints', [])
    else:
        print(f"Erreur lors de la requête à l'API: {response.status_code}")
        return []


# Exemple d'utilisation
foods = get_nutritional_value_by_ingredients()

for food in foods:
    print(f"Plats: {food['food']['label']}")
    print(f"Valeurs nutritionnelles: {food['food']['nutrients']}")
    print("-----")
