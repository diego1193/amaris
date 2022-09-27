from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import requests

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def get_pokemons(request, pk):
    if request.method == 'GET':
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{pk}/", params={})
        if response.status_code == 200:
            response_json = response.json()
            name = response_json["pokemon"]["name"]
            return JsonResponse({"name": name}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"Error": "id del pokemon incorrecto"}, status=status.HTTP_400_BAD_REQUEST)
