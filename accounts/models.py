from django.db import models
from django import forms
from django.contrib.auth.models import User
from tarifas.models import *


ATRIBUICOES_ESCOLHAS = [
    ('','Atribuição'),
    ('Administrador', 'Administrador'),
    ('Encarregado','Encarregado'),
    ('Porteiro', 'Porteiro'),
    ('Zelador','Zelador'),
    ('Outro','Outro')
 
]


# O cliente é o próprio condomínio
# Cadastrar preferencialmente com um email do condomínio
#COMPANHIAS = Companhia.objects.all().order_by('nome')

class Condominio(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=70,null=True)
    email = models.EmailField(null=True) # Email para contato direto
    phone = models.IntegerField(null=True) # Telefone para contato direto
    num_blocos = models.IntegerField(null=True) # numero de blocos
    zip_code = models.CharField(null=True,max_length=25) #CEP
    concessionaria = models.CharField(max_length=50,null=True) # models.ForeignKey(Companhia,null=True,on_delete=models.PROTECT)
    faixa = models.CharField(max_length=50,null=True) # models.ForeignKey(Tipo_tarifa,null=True,on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    # def parceiro(self):
    #     return self.parceiro_set().all()
    
    #def faixa(self.concessionaria):
    #    query = Tipo_tarifa.objects.filter(empresa=self.concessionaria)
    #    faixa = forms.ModelChoiceField(queryset=query)
    #    return 

class Contatos(models.Model):
    name = models.CharField(max_length=70,null=True)
    attr = models.CharField(max_length=20,null=True,choices=ATRIBUICOES_ESCOLHAS) # atribuição
    phone = models.IntegerField(blank=True)# telefone para receber o alarme por whatsapp
    email = models.EmailField(blank=True)
    cond = models.ForeignKey(Condominio,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cond} : {self.name} ({self.attr})"

    class Meta:
        verbose_name = 'Contato para alarme e aviso'
        verbose_name_plural = 'Contatos para alarme e aviso'

class Parceiro(models.Model):
    nome = models.CharField(max_length=70,null=True)
    monitorados = models.ManyToManyField(Condominio)

    def __str__(self):
        return self.nome
