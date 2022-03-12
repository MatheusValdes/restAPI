from django.contrib import admin
from .models import *


class CompanhiaAdmin(admin.ModelAdmin):
    list_display = ['nome','estado','cadastro_fim']
    
class Tipo_tarifaAdmin(admin.ModelAdmin):
    list_display = ['tarifa','empresa','slug']
    list_filter=['empresa']
    
class FaixasAdmin(admin.ModelAdmin):
    list_display = ['__str__','data']
    
    
        

admin.site.register(Companhia,CompanhiaAdmin)
admin.site.register(Faixas,FaixasAdmin)
admin.site.register(Tipo_tarifa,Tipo_tarifaAdmin)
