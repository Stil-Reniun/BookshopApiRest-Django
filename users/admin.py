from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import UserModel

@admin.register(UserModel)
class UserAdmin(BaseUserAdmin):
    pass

