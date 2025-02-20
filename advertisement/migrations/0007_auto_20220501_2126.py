# Generated by Django 3.2 on 2022-05-01 21:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("advertisement", "0006_rename_profile_advertisement_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvertisementImage",
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
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("modified_time", models.DateTimeField(auto_now=True)),
                (
                    "image_file",
                    models.FileField(
                        upload_to="images/advertisement/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=("jpg", "png", "jpeg")
                            )
                        ],
                    ),
                ),
                (
                    "advertisement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="advertisement.advertisement",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="Image",
        ),
    ]
