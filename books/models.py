from django.db import models
from django.db.models import SET_NULL
from users.models import UserModel
from genre.models import Genre

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='books/images/')
    author = models.CharField(max_length=255)
    synopsis = models.TextField(max_length=1000)
    editorial = models.CharField(max_length=255)
    dayPublication = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    pages = models.IntegerField()
    formats =  models.CharField(max_length=255)
    isbn = models.CharField(max_length=15)
    document = models.URLField()
    language =  models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    statusk = models.CharField(max_length=20)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title