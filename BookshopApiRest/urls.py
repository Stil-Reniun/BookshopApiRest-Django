from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from genre.api.router import router_genres
from books.api.router import router_books
from comments.api.router import router_comments

schema_view = get_schema_view(
    openapi.Info(
        title="Bookshop API REST",
        default_version='v1',
        description="Bookshop REST API for online book management",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="solisaullajuan@gmail"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_books.urls)),
    path('api/', include(router_genres.urls)),
    path('api/', include(router_comments.urls))
]
