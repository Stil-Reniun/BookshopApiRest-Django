from rest_framework.viewsets import ModelViewSet
from books.models import Book
from django_filters.rest_framework import DjangoFilterBackend
from  books.api.serializer import BooksSerializer
from books.api.permission import IsAdminOrReadOnly

class BooksApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BooksSerializer
    queryset = Book.objects.filter(published=True)
    filter_backends = [DjangoFilterBackend]
    filtersets_fields =['genre',]