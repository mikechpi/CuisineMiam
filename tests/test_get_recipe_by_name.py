from get_recipe_by_name import get_recipe_by_name

def test_GetRecipeByName_succes(monkeypatch):
    monkeypatch.setenv("baseUrl",
                       "https://api.edamam.com/api/recipes/v2")
    monkeypatch.setenv("apiKey",
                       "46df1aff8431edce2ce1f40a0b9bb08e")
    monkeypatch.setenv("apiId",
                       "9c60bb8a")

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
                                ["pizza"]}}]}, 200)

    monkeypatch.setattr("requests.get", mock_get)

    recipe_name = "pizza"
    recipes = get_recipe_by_name(recipe_name)
    assert len(recipes) == 1
    assert recipes[0]['recipe']['label'] == "Test Recipe"
    assert recipes[0]['recipe']['ingredientLines'] == ["pizza"]


def test_GetRecipeByName_failure(monkeypatch, capsys):
    monkeypatch.setenv("baseUrl",
                       "https://api.edamam.com/api/recipes/v2")
    monkeypatch.setenv("apiKey",
                       "46df1aff8431edce2ce1f40a0b9bb08e")
    monkeypatch.setenv("apiId",
                       "9c60bb8a")

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_get(url):
        return MockResponse(None, 404)

    monkeypatch.setattr("requests.get", mock_get)

    recipes_name = ""
    recipes = get_recipe_by_name(recipes_name)
    captured = capsys.readouterr()
    assert recipes == []
    assert "Erreur lors de la requête à l'API: 404" in captured.out
