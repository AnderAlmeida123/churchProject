from django.db import models

from core.models import BaseResponsavelModel
from pessoas.models import Pessoa
from setores.models import Setor


class MembroSetor(BaseResponsavelModel):
    data_entrada = models.DateField(
        verbose_name='Data de entrada',
    )

    data_saida = models.DateField(
        verbose_name='Data de saida',

    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        verbose_name='pessoa',
        related_name='membro_setor',
    )

    setor = models.ForeignKey(
        Setor,
        on_delete=models.PROTECT,
        verbose_name='Setor',
        related_name='setor_nome',
    )

    class Meta:
        verbose_name = 'Membro Setor'
        verbose_name_plural = 'Membros Setores'

    @property
    def data_entrada_formatada(self):
        return self.data_entrada.strftime('%d/%m/%Y') if self.data_entrada else None

    @property
    def data_saida_formatada(self):
        return self.data_saida.strftime('%d/%m/%Y') if self.data_saida else None

    def __str__(self):
        return f'{self.pessoa} - {self.setor}'