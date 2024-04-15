from nutrition_api import NutritionAPI


def test_nutritionApi_success(monkeypatch):
    # Mocking variables
    monkeypatch.setenv("apiKey",
                       "b39187147c75cca26f694bdf7bae8958")
    monkeypatch.setenv("apiId",
                       "a4e84092")

    # Mocking requests.get function
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_get(url):
        return MockResponse({"dietLabels": ["Low-Carb"],
                            "co2EmissionsClass": "A",
                             "calories": 250}, 200)

    monkeypatch.setattr("requests.get", mock_get)

    # Test
    ingredients = "steak"
    recipes = NutritionAPI.get_nutritional_value_by_ingredients(ingredients)
    assert len(recipes) == 3
    assert recipes['dietLabels'] == ["Low-Carb"]
    assert recipes['co2EmissionsClass'] == "A"
    assert recipes['calories'] == 250
