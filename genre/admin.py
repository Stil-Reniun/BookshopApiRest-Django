from django.contrib import admin
from genre.models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']
