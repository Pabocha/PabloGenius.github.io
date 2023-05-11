from django.contrib import admin
from .models import Utilisateur
from .forms import UserCreationForms, MyUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class AdminUser(UserAdmin):
    add_form = UserCreationForms
    form = MyUserChangeForm

    list_display = ['username', 'first_name',
                    'last_name', 'email', 'phone', 'membre', 'budget']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Info Personnel', {'fields': ('first_name',
         'last_name', 'email', 'phone', 'adresse', 'image_de_profile')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Inscription', {'fields': ('budget', 'membre')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'phone', 'adresse'),
        }),
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(Utilisateur, AdminUser)
