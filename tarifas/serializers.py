from rest_framework import serializers

from .models import Companhia, Tipo_tarifa, Faixas

class CompanhiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companhia
        fields = '__all__'

class TarifasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_tarifa
        fields = '__all__'

class FaixasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faixas
        fields = '__all__'