from django.db import models
from core.models import BaseResponsavelModel


class Setor(BaseResponsavelModel):
    nome_setor = models.CharField(
        max_length=100,
        verbose_name='Nome do Setor',
    )

    descricao = models.TextField(
        blank=True,
        verbose_name='Descrição do setor'
    )

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.nome_setor
