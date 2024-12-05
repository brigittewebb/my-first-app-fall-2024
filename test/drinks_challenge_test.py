from app.drinks_challenge import fetch_drinks_json

def test_data_fetching():
    data = fetch_drinks_json()
    assert isinstance(data, list)
    assert len(data) == 20