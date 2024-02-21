from rest_framework.routers import DefaultRouter
from genre.api.views import GenreApiViewSet

router_genres = DefaultRouter()
router_genres.register(prefix='genres', basename='genres', viewset=GenreApiViewSet)