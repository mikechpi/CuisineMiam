from getNameRecipes import getNameRecipesByNameIngredients


def test_GetNameRecipesByNameIngredients_success(monkeypatch):
    # Mocking variables
    monkeypatch.setenv("baseUrl",
                       "https://api.edamam.com/api/recipes/v2?type=public")
    monkeypatch.setenv("apiKey",
                       "5c0e46d6a1d3106ff55a5e2925e27f76")
    monkeypatch.setenv("apiId",
                       "8a33a29b")

    # Mocking requests.get function
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_get(url):
        return MockResponse({"hits":
                             [{"recipe":
                               {"label": "Test Recipe", "ingredientLines":
                                ["tomate", "salade"]}}]}, 200)

    monkeypatch.setattr("requests.get", mock_get)

    # Test
    ingredients = ["tomate", "salade"]
    recipes = getNameRecipesByNameIngredients(ingredients)
    assert len(recipes) == 1
    assert recipes[0]['recipe']['label'] == "Test Recipe"
    assert recipes[0]['recipe']['ingredientLines'] == ["tomate", "salade"]


def test_getNameRecipesByNameIngredients_failure(monkeypatch, capsys):
    # Mocking variables
    monkeypatch.setenv("baseUrl", "your_base_url")
    monkeypatch.setenv("apiKey", "your_api_key")
    monkeypatch.setenv("apiId", "your_api_id")

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    # Mocking the requests.get function
    def mock_get(url):
        return MockResponse(None, 404)

    monkeypatch.setattr("requests.get", mock_get)

    # Test
    ingredients = ["ingredient1", "ingredient2"]
    recipes = getNameRecipesByNameIngredients(ingredients)
    captured = capsys.readouterr()
    assert recipes == []
    assert "Erreur lors de la requête à l'API: 404" in captured.out
