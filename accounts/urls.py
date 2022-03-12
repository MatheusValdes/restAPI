from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    #path('clientes/list/', views.ClienteList.as_view()),
    #path('clientes/list/2', views.DadosCliente,name='algo'),
    path("admin/condominio/",views.CondominioAdminListar.as_view()),
    path("admin/contato/",views.ContatosAdminListar.as_view()),
    path("condominio/",views.Condominios.as_view()),
    path("condominio/<int:pk>/",views.CondominioDetail.as_view()),
    path("contato/",views.ContatosList.as_view()),
    path("contato/<int:pk>/",views.ContatosDetail.as_view()),

#     path('clientes/cond/list/', views.CondClienteList),
#     path('clientes/cond/create/', views.CondCreate.as_view()),
# ###################### CONTATO
#     path('clientes/cond/contatos/list/',views.CondContactList),
#     path('teste/',views.teste)

]