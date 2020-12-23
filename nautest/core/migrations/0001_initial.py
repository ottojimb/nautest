"""Migrations for django project."""
# Generated by Django 3.1.4 on 2020-12-23 18:12
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    """Class to define migration."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QueryLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("query_string", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        )
    ]
