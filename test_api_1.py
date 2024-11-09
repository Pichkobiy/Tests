import requests
import pytest

token = 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMTQ2NTQ5LCJpYXQiOjE3MzA5OTIzODksImV4cCI6MTczMDk5NTk4OSwidHlwZSI6MjB9.dihxTy2qZb7feLP084fSjVu681bJBdl6mJl1jeKxYF8'
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

body = {
    "id":134243402,
    "quantity":2
}

def test_put():
    url = 'https://web-gate.chitai-gorod.ru/api/v2/cart'
    response = requests.put(url, headers=headers, json=body)

    assert response.status_code == 200
    assert 'content' in response.json()    

def test_delete():
    url = 'https://web-gate.chitai-gorod.ru/api/v2/cart/product/134420243'
    response = requests.delete(url, headers=headers)

    assert response.status_code == 404    
