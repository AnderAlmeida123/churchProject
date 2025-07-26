from django.db import models

from core.models import BaseResponsavelModel
from pessoas.models import Pessoa
from turmas.models import Turma


class MembroTurma(BaseResponsavelModel):
    data_entrada = models.DateField(
        verbose_name='Data de entrada',
        auto_now=False,
        auto_now_add=False,
    )

    data_saida = models.DateField(
        verbose_name='Data de saida',
        auto_now=False,
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        verbose_name='pessoa',
        related_name='membro_turma',
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.PROTECT,
        verbose_name='Turma',
        related_name='turmas_nome',
    )

    class Meta:
        verbose_name = 'Membro Turma'
        verbose_name_plural = 'Membros Turmas'

    @property
    def data_entrada_formatada(self):
        return self.data_entrada.strftime('%d/%m/%Y') if self.data_entrada else None

    @property
    def data_saida_formatada(self):
        return self.data_saida.strftime('%d/%m/%y') if self.data_saida else None

    def __str__(self):
        return f'{self.pessoa} - {self.turma}'
