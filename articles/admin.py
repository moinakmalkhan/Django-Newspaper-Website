from django.contrib import admin
from .models import Category, Articles
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
