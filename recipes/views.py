from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all().order_by('-id') #Mosrtra na tela todas as receitas cadastradas no DB por ordem descrescente de id
    return render(request,'recipes/pages/home.html',context={
        'recipes': recipes #Manda para o template home.html a variável instanciada na ln 6
    })

def recipe(request, id):
    recipee = Recipe.objects.get(id=id) # id do parametro da função será igual o id do Recipe.object. A pagina só mostrará uma unica receita cujo os ids são iguais
    return render(request, 'recipes/pages/recipe-view.html',context={
        'recipe': recipee,
        'is_datail_page':True,# retira botão caso seja pagina de detalhes
        })