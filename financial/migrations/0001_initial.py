# Generated by Django 3.2 on 2022-06-06 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Gateway",
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
                    models.CharField(max_length=180, verbose_name="gateway title"),
                ),
                (
                    "gateway_request_url",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="request url",
                    ),
                ),
                (
                    "gateway_verify_url",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="verify url"
                    ),
                ),
                (
                    "gateway_code",
                    models.CharField(
                        choices=[("zarinpal", "Zarinpal")],
                        max_length=12,
                        verbose_name="gateway code",
                    ),
                ),
                (
                    "is_enable",
                    models.BooleanField(default=True, verbose_name="is enable"),
                ),
                (
                    "auth_data",
                    models.TextField(blank=True, null=True, verbose_name="auth data"),
                ),
            ],
            options={
                "verbose_name": "Gateway",
                "verbose_name_plural": "Gateways",
            },
        ),
        migrations.CreateModel(
            name="Payment",
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
                    "invoice_number",
                    models.UUIDField(
                        default=uuid.UUID("b4ebb5ca-f979-46c7-8f99-802fba1fee01"),
                        verbose_name="invoice number",
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="amount")),
                ("is_paid", models.BooleanField(default=False, verbose_name="is paid")),
                ("payment_log", models.TextField(blank=True, verbose_name="log")),
                (
                    "authority",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="authority"
                    ),
                ),
                (
                    "gateway",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to="financial.gateway",
                        verbose_name="gateway",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="payments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Payment",
                "verbose_name_plural": "Payments",
            },
        ),
    ]
