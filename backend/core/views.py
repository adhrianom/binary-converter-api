from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import float_to_binary_iee

class ConverterAPIView(APIView):
    def post(self, request):
        ## pega o numero enviado no JSON
        num = request.data.get('number')
        if num is None:
            return Response({'error': 'Campo "number" não fornecido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            num = float(num)
        except ValueError:
            return Response({'error': 'Valor inválido. Por favor, envie um número válido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        ## Chama a função de conversão

        result = float_to_binary_iee(num)
        return Response({
            "number_received": num,
            "ieee754": result
        })