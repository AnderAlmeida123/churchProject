# Generated by Django 5.2.1 on 2025-07-06 21:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Produto",
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
                    "nome",
                    models.CharField(max_length=100, verbose_name="Nome do Produto"),
                ),
                (
                    "categoria",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Categoria"
                    ),
                ),
                (
                    "descricao",
                    models.TextField(blank=True, null=True, verbose_name="Descrição"),
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
                "verbose_name": "Produto",
                "verbose_name_plural": "Produtos",
                "ordering": ["nome"],
            },
        ),
    ]
