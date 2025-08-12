from django.db import models
from core.models import BaseResponsavelModel
from produtos.models import Produto
from setores.models import Setor


class MovimentacaoProduto(BaseResponsavelModel):
    ENTRADA = 'entrada'
    SAIDA = 'saida'

    TIPO_CHOICES = (
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída'),
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT
    )

    quantidade = models.PositiveIntegerField(
    )

    setor_destino = models.ForeignKey(
        Setor,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    observacao = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Movimento de Estoque'
        verbose_name_plural = 'Movimentos de Estoque'
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.tipo.upper()} - {self.produto} - {self.quantidade}"
