from rest_framework import serializers
from books.models import Book
from users.api.serializer import UserSerializer
from genre.api.serializer import GenreSerializer

class BooksSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    genre = GenreSerializer()
    class Meta:
        model = Book
        fields = '__all__'