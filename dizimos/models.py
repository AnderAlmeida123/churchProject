from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

from core.models import BaseResponsavelModel
from pessoas.models import Pessoa  # Ajuste conforme o local do seu model Pessoa


class Dizimo(BaseResponsavelModel):
    mes = models.CharField(
        max_length=20,
        verbose_name="Mês",
        help_text="Informe o mês de referência do dízimo."
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Valor"
    )

    tipo_pagamento = models.CharField(
        max_length=50,
        verbose_name="Tipo de Pagamento"
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        related_name="dizimos",
        verbose_name="Pessoa"
    )

    class Meta:
        verbose_name = "Dízimo"
        verbose_name_plural = "Dízimos"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.pessoa} - {self.mes} - R$ {self.valor}"
