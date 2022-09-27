from django.test import TestCase
from django.test import Client

def test_punto():
        
    c = Client()
    response = c.get('http://127.0.0.1:8080/pockemon/1/')
    assert response.status_code == 201 and response.json() == {"name": "bulbasaur"}