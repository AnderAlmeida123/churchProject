from django.db import models
from django.db.models.fields import DateTimeField
from comunidades.models import Comunidade
from tipoEventos.models import TipoEvento


class Calendario(models.Model):
    titulo_evento = models.CharField(
        max_length=100,
        verbose_name='Título do Evento'
    )

    data_hora = models.DateTimeField(
        verbose_name='Data e Hora do Evento'
    )

    descricao = models.TextField(
        verbose_name='Descrição do Evento'
    )

    comunidade = models.ForeignKey(
        Comunidade,
        on_delete=models.PROTECT,
        related_name='eventos',
        verbose_name='Comunidade'
    )

    tipo_evento = models.ForeignKey(
        TipoEvento,
        on_delete=models.PROTECT,
        related_name='eventos',
        verbose_name='Tipo de Evento'
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
        verbose_name = 'Evento no Calendário'
        verbose_name_plural = 'Eventos no Calendário'
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.titulo_evento} - {self.descricao} - {self.comunidade} - {self.tipo_evento}"
