from django.db import models

from comunidades.models import Comunidade
from core.models import BaseResponsavelModel
from pessoas.models import Pessoa
from tipoSacramentos.models import TipoSacramento


class Sacramento(BaseResponsavelModel):
    data_hora = models.DateTimeField(
        max_length=100,
        verbose_name="Data e Hora do Sacramento",
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        verbose_name="Pessoa",
        help_text="Pessoa do Sacramento",
    )

    comunidade = models.ForeignKey(
        Comunidade,
        on_delete=models.PROTECT,
        verbose_name="Comunidade",
        help_text="Comunidade do Sacramento",
    )

    tipo_sacramento = models.ForeignKey(
        TipoSacramento,
        on_delete=models.PROTECT,
        verbose_name="Tipo Sacramento",
        help_text="Tipo Sacramento do Sacramento",
    )

    class Meta:
        verbose_name = "Sacramento"
        verbose_name_plural = "Sacramentos"

    def __str__(self):
        return f"{self.pessoa} - {self.comunidade} - {self.tipo_sacramento} - {self.data_hora}"
