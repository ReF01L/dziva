from django.contrib import admin
from .models import Category, Product, ProductMethods, ProductCharacters


class MethodsInline(admin.TabularInline):
    model = ProductMethods
    raw_id_fields = ['product']


class CharactersInline(admin.TabularInline):
    model = ProductCharacters
    raw_id_fields = ['product']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'updated', 'structure')
    list_editable = ('price', 'available', 'structure')
    list_filter = ('available', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (MethodsInline, CharactersInline)
