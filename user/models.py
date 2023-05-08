import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

from authentication.models import User



class Income(models.Model):
   
    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    nameOfRevenue = models.CharField(_("Name Of Revenue"), max_length=255, blank=False, null=False)
    amount = models.IntegerField(_("Amount"), default=0, validators=[MaxValueValidator(9999999999)])
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
    
    def __str__(self):
        return f"{self.nameOfRevenue} | {self.amount}"


class Expenditure(models.Model):
    Category = (
        ("food", "Food"),
        ("transportation", "Transportation"),
        ("dress", "Dress"),
        ("fuel", "Fuel")
    )
    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    category = models.CharField(max_length=100, choices=Category)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    nameOfItem = models.CharField(_("Name Of Item"), max_length=255, blank=True, null=True)
    estimatedAmount = models.IntegerField(_("Estimated Amount"), default=0, validators=[MaxValueValidator(9999999999)])
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
    
    def __str__(self):
        return f"{self.nameOfItem} | {self.estimatedAmount}"