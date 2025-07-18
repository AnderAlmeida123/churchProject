from django.db import models
from core.models import BaseResponsavelModel


class Produto(BaseResponsavelModel):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do Produto"
    )

    categoria = models.CharField(
        max_length=100,
        verbose_name="Categoria",
        blank=True,
        null=True
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
