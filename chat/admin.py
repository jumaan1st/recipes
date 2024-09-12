from django.contrib import admin
from .models import Cuisine, Recipe

@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'preparation_time', 'cooking_time', 'serves')
    list_filter = ('cuisine',)
