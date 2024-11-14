import requests
import pytest
from config import *

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
body = {
    "searchPhrase":"стивен кинг",
    "resultCount":793
}

def test_post():
    
    response = requests.post(f"{baseURL}api/v2/search/results", headers=headers, json=body)

    assert response.status_code == 204
    

def test_get():
    
    response = requests.get(f"{baseURL}api/v2/categories", headers=headers)

    assert response.status_code == 200   

def test_get_2():
    
    response = requests.get(f"{baseURL}api/v1/products/slug/fairy-tale-3027523", headers=headers)

    assert response.status_code == 200   

body_2 = {
    "id":134243402,
    "quantity":2
}

def test_put():
    
    response = requests.put(f"{baseURL}api/v1/cart", headers=headers, json=body_2)

    assert response.status_code == 200
      

def test_delete():
    
    response = requests.delete(f"{baseURL}api/v1/cart/product/134420243", headers=headers)

    assert response.status_code == 404    
