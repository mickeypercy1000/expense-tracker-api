# Generated by Django 4.1.7 on 2023-03-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_alter_expenditure_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expenditure",
            name="category",
            field=models.CharField(
                choices=[
                    ("food", "Food"),
                    ("transportation", "Transportation"),
                    ("dress", "Dress"),
                    ("fuel", "Fuel"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="income",
            name="nameOfRevenue",
            field=models.CharField(
                default="", max_length=255, verbose_name="Name Of Revenue"
            ),
            preserve_default=False,
        ),
    ]