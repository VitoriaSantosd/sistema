from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario_geral, name='calendario_geral'),
    path('calendario_filtrado/', views.calendario_filtrado_view, name='calendario_filtrado'),
]
