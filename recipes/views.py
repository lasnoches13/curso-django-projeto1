from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe


def category(request,category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id') #category é um atributo do tipo foreignkey de Recipe(models ln 39), por tanto é necessário chamar o id da categoria aqui dentro de Recipe.objects através de {atributo+underline duplo+id} e filtrar com o id passado como arquimento na função. (id da receita clicada/escolhida na home)
    return render(request,'recipes/pages/home.html',context={
        'recipes': recipes #Manda para o template home.html a variável instanciada na ln 6
    })

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id') #Mosrtra na tela todas as receitas cadastradas no DB por ordem descrescente de id
    return render(request,'recipes/pages/home.html',context={
        'recipes': recipes #Manda para o template home.html a variável instanciada na ln 6 para ser usada em loop for. Esse loop vai listar todas as receitas contidas na variável instanciada
    })

def recipe(request, id):
    recipee = Recipe.objects.get(id=id) # id do parametro da função será igual o id do Recipe.objects... A pagina só mostrará uma unica receita cujo os ids são iguais
    return render(request, 'recipes/pages/recipe-view.html',context={
        'recipe': recipee,
        'is_datail_page':True,# retira botão caso seja pagina de detalhes
        })