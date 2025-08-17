from django.db import models
from core.models import BaseResponsavelModel
from pessoas.models import Pessoa


class Turma(BaseResponsavelModel):
    nome_turma = models.CharField(
        verbose_name='nome da turma',
        max_length=100
    )

    descricao = models.CharField(
        verbose_name='descricao',
        max_length=100
    )

    class Meta:
        verbose_name = 'turma'
        verbose_name_plural = 'turmas'

    def __str__(self):
        return f'{self.nome_turma}'
