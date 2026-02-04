#verify on admin.py the models that will be on the admin webpage
# adicionar em admin.py as classes que aparecerão na pagina web ADMIN

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

# para retornar o nome da categoria na pagina admin. caso contrario apareciria 'object(id)'
    def __str__(self): 
        return self.name
    
# opções de escolha na hora de criar a receita: unidade no tempo de preparo e unidade no rendimento   
class Preparation_time_unit(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Serving_units(models.Model):
    name = models.CharField(max_length = 10)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length = 65)
    description = models.CharField(max_length = 165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.ForeignKey(Preparation_time_unit,on_delete = models.SET_NULL,null=True)
    servings = models.IntegerField()
    servings_unit = models.ForeignKey(Serving_units, on_delete = models.SET_NULL,null=True)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='Recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True, default=None)
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.title

# Category: quando apagado alguuma categoria as receitas que são da ccategoria não serão apagadas (SET.NULL) e será possivel atualizar informações no admin sem ser obrigatorio adicionar categoria (blank=True e default =None)