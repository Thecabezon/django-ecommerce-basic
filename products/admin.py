from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at') # Mostrar nombre y fecha de creación

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at') # Mostrar categoría en la lista
    list_filter = ('category',) # Filtro por categoría