from django.contrib import admin
from .models import Category, Book


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category']
    search_fields = ('name', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
