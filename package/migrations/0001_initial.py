# Generated by Django 3.2 on 2022-06-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Package",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=48, verbose_name="package title"),
                ),
                ("price", models.PositiveBigIntegerField(verbose_name="package price")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="package description"),
                ),
                ("days", models.PositiveSmallIntegerField(verbose_name="package days")),
                ("is_enable", models.BooleanField(default=True)),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("modified_time", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
