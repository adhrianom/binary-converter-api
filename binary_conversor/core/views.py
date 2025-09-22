from django.shortcuts import render
from django.http import HttpResponse
from .utils import float_to_binary_iee
from django.http import JsonResponse

# Create your views here.
def converter(request):
    try:
        numero = float(request.GET.get('numero', 0)) # pega o numero da URL
        resultado = float_to_binary_iee(numero)
        return JsonResponse(resultado)
    except ValueError:
        return JsonResponse({"error": "Número inválido"}, status=400)