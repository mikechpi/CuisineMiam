from nutritionalValue import get_nutritional_value_by_ingredients


def test_get_nutritional_value_by_ingredients():
    foods = get_nutritional_value_by_ingredients()
    assert len(foods) > 0
    for food in foods:
        assert 'label' in food['food']
        assert 'nutrients' in food['food']
