# Generated by Django 4.1.7 on 2023-03-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_rename_user_name_user_username_user_firstname_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]