from django.shortcuts import render
from utils.recipes.factory import make_recipe

def home(request):
    return render(request,'recipes/pages/home.html',context={
        'recipes': [make_recipe() for _ in range(10)],#envia para home.html linha 07
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html',context={
        'recipe':make_recipe(),#faker
        'is_datail_page':True,# retira botão caso seja pagina de detalhes
        })