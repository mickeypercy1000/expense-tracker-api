from django.contrib import admin
from user.models import Expenditure, Income, User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    username = forms.CharField(max_length=30, required=True)
    model = User

    list_display = (
            "email",
            "firstname",
            "lastname",
            "username",
            "is_superuser",
        )
    search_fields = ("firstname", "lastname", "email", "username")
    list_filter = ("firstname", "lastname", "email", "username")
    readonly_fields = (
        "created_at",
        "updated_at",
    )

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

# admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Income)
admin.site.register(Expenditure)
