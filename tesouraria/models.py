from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from decimal import Decimal
from core.models import BaseResponsavelModel


class Tesouraria(BaseResponsavelModel):
    TIPO_MOVIMENTACAO_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )

    tipo_movimentacao = models.CharField(
        max_length=50,
        choices=TIPO_MOVIMENTACAO_CHOICES,
        verbose_name="Tipo de Movimentação"
    )

    descricao = models.CharField(
        max_length=255,
        verbose_name="Descrição"
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Valor"
    )

    data_movimentacao = models.DateField(
        verbose_name="Data da Movimentação"
    )

    entrada_saida = models.BooleanField(
        verbose_name="Entrada ou Saída"
    )

    setor = models.ForeignKey(
        'setores.Setor',
        on_delete=models.PROTECT,
        verbose_name="Setor"
    )

    class Meta:
        verbose_name = "Movimentação Financeira"
        verbose_name_plural = "Movimentações Financeiras"
        ordering = ["-data_movimentacao"]

    def __str__(self):
        tipo = "Entrada" if self.entrada_saida else "Saída"
        return f"{tipo} - {self.descricao} - R$ {self.valor}"
