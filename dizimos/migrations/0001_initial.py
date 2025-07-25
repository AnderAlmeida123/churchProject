# Generated by Django 5.2.1 on 2025-07-06 21:55

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pessoas", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Dizimo",
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
                    "criado_em",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "atualizado_em",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo")),
                (
                    "mes",
                    models.CharField(
                        help_text="Informe o mês de referência do dízimo.",
                        max_length=20,
                        verbose_name="Mês",
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.01"))
                        ],
                        verbose_name="Valor",
                    ),
                ),
                (
                    "tipo_pagamento",
                    models.CharField(max_length=50, verbose_name="Tipo de Pagamento"),
                ),
                (
                    "pessoa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="dizimos",
                        to="pessoas.pessoa",
                        verbose_name="Pessoa",
                    ),
                ),
                (
                    "responsavel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_responsavel",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Responsável",
                    ),
                ),
            ],
            options={
                "verbose_name": "Dízimo",
                "verbose_name_plural": "Dízimos",
                "ordering": ["-criado_em"],
            },
        ),
    ]
