from rest_framework.routers import DefaultRouter
from books.api.views import  BooksApiViewSet

router_books = DefaultRouter()
router_books.register(prefix='books', basename='books', viewset=BooksApiViewSet)