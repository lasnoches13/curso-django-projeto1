from django.contrib import admin
from .models import Category,Recipe,Serving_units,Preparation_time_unit

class CategoryAdmin(admin.ModelAdmin):
    ...
class RecipeAdmin(admin.ModelAdmin):
    ...
class Serving_units_Admin(admin.ModelAdmin):
    ...
class Preparation_time_unit_Admin(admin.ModelAdmin):
    ...
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Serving_units,Serving_units_Admin)
admin.site.register(Preparation_time_unit,Serving_units_Admin)