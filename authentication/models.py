import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.managers import CustomUserManager
from django.core.validators import MaxValueValidator



class User(AbstractUser):
   
    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    firstname = models.CharField(_("First name"), max_length=255, blank=True, null=True)
    lastname = models.CharField(_("Last name"), max_length=255, blank=True, null=True)
    username = models.CharField(_("Username"), max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(_("Email"), unique=True, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname"]

    class Meta:
        ordering = ("-created_at",)
    
    def __str__(self):
        return f"{self.firstname} | {self.lastname} | {str(self.email)}"

    def get_email(self):
        return self.email