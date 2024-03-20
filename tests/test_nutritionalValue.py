from nutritionalValue import Nutrition


def test_get_nutritional_value_by_ingredients(monkeypatch):
    # Mocking variables
    monkeypatch.setenv("baseUrl",
                       "https://api.edamam.com/api/food-database/v2/parser?")
    monkeypatch.setenv("apiKey",
                       "eb6ea35df7c8575bc23b17d0c36e1706")
    monkeypatch.setenv("apiId",
                       "4a23515f")
    
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
        
    def mock_get(url):
        return MockResponse({"hints":
                             [{"food":
                               {"label": "Egg", "nutrients":
                                {'ENERC_KCAL': 143.0, 'PROCNT': 12.6, 'FAT': 9.51, 'CHOCDF': 0.72, 'FIBTG': 0.0}}}]}, 200)

    monkeypatch.setattr("requests.get", mock_get)

    # Test
    ingredient = "Egg"
    recipes = Nutrition.get_nutritional_value_by_ingredients(ingredient)
    assert len(recipes) > 0
    assert recipes[0]['food']['label'] == "Egg"
    assert recipes[0]['food']['nutrients'] == {'ENERC_KCAL': 143.0, 'PROCNT': 12.6, 'FAT': 9.51, 'CHOCDF': 0.72, 'FIBTG': 0.0}


def test_display_foods(capfd):
    foods = [
        {'food':
            {'label': 'Egg', 'nutrients':
                {'ENERC_KCAL': 143.0,
                 'PROCNT': 12.6, 'FAT': 9.51, 'CHOCDF': 0.72, 'FIBTG': 0.0}
             }
         },
        {'food':
            {'label': 'Free Range & Organic Egg', 'nutrients':
                {'ENERC_KCAL': 143.0,
                 'PROCNT': 12.6, 'FAT': 9.51, 'CHOCDF': 0.72, 'FIBTG': 0.0}
             }
         }
    ]

    Nutrition.display_food(foods)

    captured = capfd.readouterr()

    expected_output = (
        "Plats: Egg\nValeurs nutritionnelles:" +
        " {'ENERC_KCAL': 143.0, 'PROCNT': 12.6, 'FAT': 9.51," +
        " 'CHOCDF': 0.72, 'FIBTG': 0.0}\n-----\n" +
        "Plats: Free Range & Organic Egg\nValeurs nutritionnelles:" +
        " {'ENERC_KCAL': 143.0, 'PROCNT': 12.6, 'FAT': 9.51," +
        " 'CHOCDF': 0.72, 'FIBTG': 0.0}\n-----\n"
    )

    assert captured.out == expected_output
