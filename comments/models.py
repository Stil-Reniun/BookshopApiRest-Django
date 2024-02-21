from django.db import models
from django.db.models import CASCADE
from books.models import Book
from users.models import UserModel

class Comment(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=CASCADE, null=True)