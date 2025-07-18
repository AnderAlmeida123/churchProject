from django.db import models
from core.models import BaseResponsavelModel
from pessoas.models import Pessoa


class Setor(BaseResponsavelModel):
    nome_setor = models.CharField(
        max_length=100,
        verbose_name='Nome do Setor',
    )

    descricao = models.TextField(
        blank=True,
        verbose_name='Descrição do setor'
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        verbose_name='pessoa',
        related_name='setor'
    )

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return f'{self.pessoa} - {self.nome_setor}'
