from rest_framework import serializers

from .models import Condominio, Contatos

#class ClienteSerializer2(serializers.ModelSerializer):
#    class Meta:
#        model=Cliente
#        fields = ("name",)

#class ClienteSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Cliente
#        fields = (
#            "id",
#            # "user",
#            "name",
#            "phone",
#            "email",
#            "date_created",
#            #"pago",
            # "pago_em",
            # "valido_ate"
#        )

class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contatos
        fields = '__all__'
        

class CondominioSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True,many=True)
    class Meta:
        model = Condominio
        fields = (
            "user",
            "id",
            "name",
            "phone",
            "email",
            "num_blocos",
            "zip_code",
            "concessionaria",
            "faixa",
            "date_created",
            "parceiro_set"
            
        )
        depth = 1