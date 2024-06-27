from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

word_list = {"words": ["batman", "robin", "coringa"]}
invalid_word_list = {}
sort_word_list_asc = {**word_list, "order": "asc"}
sort_word_list_desc = {**word_list, "order": "desc"}
number_list = {"words": [1, 2, 3]}
invalid_datatype_error_message = "Input should be a valid string: words"
missing_field_message = "Field required: "

# vowel_count testing

def test_vowel_count():
    response = client.post("/api/vowel_count", json=word_list)
    assert response.status_code == 200
    assert response.json() == {"batman": 2, "robin": 2, "coringa": 3}


def test_reject_wrong_data_type():
    response = client.post("/api/vowel_count", json=number_list)
    assert response.status_code == 422
    assert response.json()["error"][0] == invalid_datatype_error_message


def test_reject_missing_word_list():
    response = client.post("/api/vowel_count", json=invalid_word_list)
    assert response.status_code == 422
    assert response.json()["error"][0] == missing_field_message + "words"


# sorting testing

def test_sorting_words_asc():
    response = client.post("/api/sort", json=sort_word_list_asc)
    assert response.status_code == 200
    assert response.json() == ["batman", "coringa", "robin"]

    
def test_sorting_words_desc():
    response = client.post("/api/sort", json=sort_word_list_desc)
    assert response.status_code == 200
    assert response.json() == ["robin", "coringa", "batman"]


def test_reject_sort_wrong_data_type():
    response = client.post("/api/sort", json=number_list)
    assert response.status_code == 422
    assert response.json()["error"][0] == invalid_datatype_error_message
    assert response.json()["error"][-1] == missing_field_message + "order"


def test_reject_missing_order():
    response = client.post("/api/sort", json=word_list)
    assert response.status_code == 422
    assert response.json()["error"][0] == missing_field_message + "order"

