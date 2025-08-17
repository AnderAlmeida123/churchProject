from django.db import models
from core.models import BaseResponsavelModel


class Comunidade(BaseResponsavelModel):
    nome_comunidade = models.CharField(
        max_length=100,
        verbose_name="Nome da Comunidade"
    )

    bairro = models.CharField(
        max_length=100,
        verbose_name="Bairro"
    )

    class Meta:
        verbose_name = "Comunidade"
        verbose_name_plural = "Comunidades"


    def __str__(self):
        return self.nome_comunidade
