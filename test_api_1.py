import requests
import pytest

token = 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMTQ2NTQ5LCJpYXQiOjE3MzA5OTIzODksImV4cCI6MTczMDk5NTk4OSwidHlwZSI6MjB9.dihxTy2qZb7feLP084fSjVu681bJBdl6mJl1jeKxYF8'
headers = {
"Authorization": f"Bearer {token}",
"Content-Type": "application/json"
}

def test_get():
    url = 'https://www.chitai-gorod.ru/'
    response = requests.get(url, headers=headers)

    assert response.status_code == 204
    assert 'content' in response.json()

    