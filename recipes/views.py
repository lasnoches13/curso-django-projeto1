from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
#from django.http import Http404 # levantará erro 404 caso categoria não exista ln8
from .models import Recipe

def category(request,category_id):
    # modo comum de fazer a consulta, sem usar get_list_or_404
    #<>recipes = Recipe.objects.filter(
        #category__id=category_id,
        #is_published=True).order_by('-id') 

    #category é um atributo do tipo foreignkey de Recipe(models ln 39), por tanto é necessário chamar o id da categoria aqui dentro de Recipe.objects através de {atributo+underline duplo+id} e filtrar com o id passado como arquimento na função. (id da receita clicada/escolhida na home)

    #<>if not recipes.exists(): # verifica se a consulta retornou algum resultado, caso não
    #   raise Http404("Categoria não encontrada") (desativada)
    
    #<>recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')) # get_list_or_404 
    #função desativada para evitar erro 404. Agora a página de categoria exibirá uma mensagem caso não haja receitas cadastradas na categoria selecionada.

    # é uma função do django que retorna uma lista de objetos ou levanta um erro 404 se a lista estiver vazia. Ele faz a mesma consulta que a linha 7, mas de forma mais eficiente, pois evita a necessidade de verificar manualmente se a consulta retornou resultados. Se a consulta não retornar nenhum resultado, o get_list_or_404 levantará automaticamente um erro 404, indicando que a categoria não foi encontrada. Se a consulta retornar resultados, o get_list_or_404 retornará a lista de objetos correspondentes à consulta, que pode ser usada para renderizar a página da categoria.

    recipes = (Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))

    return render(request,'recipes/pages/category.html',context={
        'recipes': recipes, #Manda para o template home.html a variável instanciada na ln 16 para ser usada em loop for. Esse loop vai listar todas as receitas contidas na variável instanciada
        #'title' : f'{recipes.first().category.name}', # nome da categoria para ser exibido na aba da página categoru ln 3
        'title' : f'{recipes.first().category.name}' if recipes else 'Categoria sem receitas' # nome da categoria para ser exibido na aba da página categoria ln 3. Se a consulta retornar resultados, o nome da categoria será exibido. Caso contrário, a mensagem "Categoria sem receitas" será exibida.
    })

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id') #Mosrtra na tela todas as receitas cadastradas no DB por ordem descrescente de id
    return render(request,'recipes/pages/home.html',context={
        'recipes': recipes #Manda para o template home.html a variável instanciada na ln 6 para ser usada em loop for. Esse loop vai listar todas as receitas contidas na variável instanciada
    })

def recipe(request, id):
    recipee = get_object_or_404(Recipe, id=id, is_published=True)
    # id do parametro da função será igual o id do Recipe.objects... A pagina só mostrará uma unica receita cujo os ids são iguais( quando o mouse passa pelo link ele ja aponta o path e o id do objeto, ao clicar a view executa a função.)

    
    return render(request, 'recipes/pages/recipe-view.html',context={
        'recipe': recipee,
        'is_datail_page':True,# retira botão caso seja pagina de detalhes
        'title': f'{recipee.title}', # objeto ja istanciado na ln19, então aqui basta chamar o atributo 'title' cadastrado no model. outra forma seria chamar por Recipe.objects.get(id=id).
        })