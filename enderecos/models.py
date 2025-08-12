from django.db import models

from core.models import BaseResponsavelModel
from pessoas.models import Pessoa


class Endereco(BaseResponsavelModel):
    cep = models.CharField(
        verbose_name='CEP',
        max_length=12,
    )
    estado = models.CharField(
        verbose_name='Estado',
        max_length=30,
    )
    cidade = models.CharField(
        verbose_name='Cidade',
        max_length=30,
    )
    bairro = models.CharField(
        verbose_name='Bairro',
        max_length=30,
    )
    rua = models.CharField(
        verbose_name='Rua',
        max_length=30,
        null=True,
        blank=True,
    )
    numero = models.CharField(
        verbose_name='Numero',
        max_length=30,
        null=True,
        blank=True,
    )
    referencia = models.CharField(
        verbose_name='Referencia',
        max_length=100,
        blank=True,
        null=True,
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        related_name='Endereco_pessoa',
        verbose_name='Pessoa',
    )

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ("-criado_em", "atualizado_em",)

    @property
    def cep_formatado(self):
        if self.cep and len(self.cep) == 8:
            return f"{self.cep[:5]}-{self.cep[5:]}"
        return self.cep

    def __str__(self):
        return f"{self.cep} - {self.estado} - {self.cidade} - {self.bairro} - {self.numero} - {self.referencia}"
