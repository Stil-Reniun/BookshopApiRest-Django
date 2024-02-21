from django.contrib import admin
from  comments.models import Comment

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'book', 'created_at']
