# Generated by Django 3.2 on 2022-06-06 03:01

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gateway",
            name="created_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gateway",
            name="modified_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="payment",
            name="created_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="payment",
            name="modified_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="payment",
            name="invoice_number",
            field=models.UUIDField(
                default=uuid.UUID("35c420f0-66c6-4803-b0c2-bfcf0c678a43"),
                verbose_name="invoice number",
            ),
        ),
    ]
