from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import (
    StaffLogin
)
# Register your models here.

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(StaffLogin)
class StaffLoginAdmin(admin.ModelAdmin):
    pass
