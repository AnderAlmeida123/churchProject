from django.db import models
from django.utils.timezone import now


class TipoEvento(models.Model):
    nome_Evento = models.CharField(
        max_length=100,
        verbose_name='Nome do Evento',
    )

    descricao = models.TextField(

    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )


class Meta:
    verbose_name = 'Tipo do Evento'
    verbose_name_plural = 'Tipos do Eventos'
    ordering = ['created_at']


def __str__(self):
    return self.nome_Evento
