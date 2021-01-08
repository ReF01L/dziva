from django.contrib import admin
from .models import Category, Product


@admin.register
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'updated')
    list_editable = ('price', 'available')
    list_filter = ('available', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}
