import requests
import pytest

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMTQ2NTQ5LCJpYXQiOjE3MzEyMjcwODEsImV4cCI6MTczMTIzMDY4MSwidHlwZSI6MjB9.H2IiTSFmzP_dbW9MYgMUh-vt8iyvag12eZ5AcQuHQK0'
headers = {
"Authorization": f"Bearer {token}",
"Content-Type": "application/json"
}
body = {
    "searchPhrase":"стивен кинг",
    "resultCount":793
}

def test_post():
    url = 'https://web-gate.chitai-gorod.ru/api/v2/search/results'
    response = requests.post(url, headers=headers, json=body)

    assert response.status_code == 204
    assert 'content' in response.json()

def test_get():
    url = 'https://web-gate.chitai-gorod.ru/api/v2/categories'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200   

def test_get_2():
    url = 'https://web-gate.chitai-gorod.ru/api/v2/products/slug/fairy-tale-3027523'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200   

body_2 = {
    "id":134243402,
    "quantity":2
}

def test_put():
    url = 'https://web-gate.chitai-gorod.ru/api/v1/cart'
    response = requests.put(url, headers=headers, json=body_2)

    assert response.status_code == 200
    assert 'content' in response.json()    

def test_delete():
    url = 'https://web-gate.chitai-gorod.ru/api/v2/cart/product/134420243'
    response = requests.delete(url, headers=headers)

    assert response.status_code == 404    
