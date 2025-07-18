from django.db import models


class TipoSacramento(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do Tipo Sacramento",
    )

    descricao = models.TextField(
        blank=True,
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
        verbose_name = "Tipo Sacramento"
        verbose_name_plural = "Tipo Sacramentos"

    def __str__(self):
        return self.nome
