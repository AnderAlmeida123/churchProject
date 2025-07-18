from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseResponsavelModel(models.Model):
    responsavel = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_responsavel",
        verbose_name="Responsável"
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em"
    )

    ativo = models.BooleanField(
        default=True,
        verbose_name="Ativo"
    )

    class Meta:
        abstract = True
