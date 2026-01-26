from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='recipes-home'),# name cria um nome proprio (string) e único para esse path. podendo ser usado em links e botões dentro do html, como em 'header.html' linha 4 
    path('recipes/<int:id>/', views.recipe, name='recipes-recipe'),
] 