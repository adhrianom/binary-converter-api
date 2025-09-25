import json
from django.shortcuts import render
from django.http import HttpResponse
from .utils import float_to_binary_iee
from django.http import JsonResponse
from .utils import float_to_binary_iee
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def converter(request):
   if request.method != 'POST':
      return JsonResponse({"error": "JSON inválido"}, status=405)
   
   try:
      body = json.loads(request.body.decode('utf-8'))
   except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
   
   num = body.get('number')
   if num is None:
        return JsonResponse({"error": "Número não fornecido"}, status=400)
   
   try:
        num = float(num)
   except ValueError:
        return JsonResponse({"error": "Número inválido"}, status=400)

   resultado = float_to_binary_iee(num)
   return JsonResponse({
       "number_received": num,
       "ieee754": resultado
   })