from django.urls import path, include
from tarifas import views

urlpatterns = [
    path('concessionarias/list/', views.ConcessionariaList.as_view()),
    path('tarifas/list/<str:empresa>/', views.TarifasList.as_view()),
    path('faixas/list/<str:empresa>/<str:tarifa>/', views.FaixasList.as_view()),
]