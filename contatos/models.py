from django.db import models
from core.models import BaseResponsavelModel
from pessoas.models import Pessoa


class Contato(BaseResponsavelModel):
    celular = models.CharField(
        max_length=15,
        blank=True,
        verbose_name='Celular',
    )
    telContato = models.CharField(
        max_length=12,
        blank=True,
        verbose_name='Telefone',
    )
    email = models.EmailField(
        blank=True,
        verbose_name='Email',
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.PROTECT,
        related_name="contato",
        verbose_name="Pessoa"
    )

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ["-criado_em"]

    @property
    def celular_formatado(self):
        if self.celular and len(self.celular) == 11:
            return f"({self.celular[:2]}) {self.celular[2:7]}-{self.celular[7:]}"
        return self.celular

    @property
    def telefone_formatado(self):
        if self.telContato and len(self.telContato) == 10:
            return f"({self.telContato[:2]}) {self.telContato[2:6]}-{self.telContato[6:]}"
        return self.telContato

    def __str__(self):
        return f"{self.celular} - {self.telContato} - {self.email} - {self.pessoa}"
