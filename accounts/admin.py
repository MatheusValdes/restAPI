from django.contrib import admin
from .models import  Condominio, Contatos, Parceiro

#class ClienteAdmin(admin.ModelAdmin):
#    list_display =  ['name','user','pago','pago_em','valido_ate','id']

admin.site.register(Contatos)
admin.site.register(Condominio)
admin.site.register(Parceiro)



