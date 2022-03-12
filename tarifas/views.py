from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView
from rest_framework import serializers, status, authentication, permissions

from .models import Companhia, Tipo_tarifa, Faixas
from .serializers import CompanhiaSerializer, TarifasSerializer, FaixasSerializer

class ConcessionariaList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # user = request.user
        cliente = Companhia.objects.all()
        serializer = CompanhiaSerializer(cliente,many=True)
        return Response(serializer.data)

class TarifasList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, empresa, format=None):
        cliente = Tipo_tarifa.objects.filter(empresa__nome=empresa)
        serializer = TarifasSerializer(cliente,many=True)
        return Response(serializer.data)

class FaixasList(APIView):

    def get(self, request,empresa, tarifa, format=None):
        print(tarifa)
        faixa = Faixas.objects.filter(tarifa__empresa__nome=empresa).filter(tarifa__slug=tarifa).order_by('-data')
        serializer = FaixasSerializer(faixa,many=True)
        return Response(serializer.data) # retorna as faixas em formato JSON, todas as faixas em ordem decrescente de data 

