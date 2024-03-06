from nutritionalValue import Nutrition


def test_get_nutritional_value_by_ingredients():
    foods = Nutrition.get_nutritional_value_by_ingredients("egg")
    assert len(foods) > 0
    for food in foods:
        assert 'label' in food['food']
        assert 'nutrients' in food['food']


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
