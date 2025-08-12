from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

from core.models import BaseResponsavelModel
from pessoas.models import Pessoa

class Dizimo(BaseResponsavelModel):
    MESES_DO_ANO = [
        ('Janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro'),
    ]

    TIPOS_PAGAMENTO = [
        ('Dinheiro', 'Dinheiro'),
        ('Pix', 'Pix'),
    ]

    mes = models.CharField(
        max_length=20,
        choices=MESES_DO_ANO,
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
        max_length=20,
        choices=TIPOS_PAGAMENTO,
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
