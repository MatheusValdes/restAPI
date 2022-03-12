from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Companhia(models.Model):
    nome = models.CharField(max_length=70,null=True)  # CAESB, SANEAGO, SABESP e etc
    estado = models.CharField(max_length=50,null=True,blank=True)
    cadastro_fim = models.BooleanField(default=False) # Todos os tipos de tarifa cadastrados?
    def __str__(self):
            return self.nome 
    
    class Meta:
        verbose_name = 'Companhia'
        verbose_name_plural = 'Companhias'


class Tipo_tarifa(models.Model):
    tarifa = models.CharField(max_length=50,null=True)# Residencial, industrial, comercial e etc
    empresa = models.ForeignKey(Companhia,null=True,on_delete=models.CASCADE)
    slug= AutoSlugField(
            populate_from='tarifa',
            unique_with='empresa__nome'
            #default='tarifa_padrao',
            )
    
    
    def __str__(self):
        return str(self.empresa) + '_' + str(self.tarifa)
    

class Faixas(models.Model):
    faixas = models.JSONField() # 
    tarifa = models.ForeignKey(Tipo_tarifa,null=True,on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=False,null=True) #data de atualizacao
    
    def __str__(self):
        return str(self.tarifa)
