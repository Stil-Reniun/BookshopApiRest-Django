from rest_framework.viewsets import  ModelViewSet
from django_filters.rest_framework import  DjangoFilterBackend
from genre.models import Genre
from genre.api.serializer import GenreSerializer
from genre.api.permissions import IsAdminOrReadOnly

class GenreApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GenreSerializer
    queryset = Genre.objects.filter(published=False)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'title']