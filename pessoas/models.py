from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.contrib.auth.models import User


class Pessoa(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='pessoa',
        verbose_name='Usuário'
    )

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome",
        blank=False,
        error_messages={
            'blank': "O Nome é obrigatório."
        }
    )

    cpf = models.CharField(
        max_length=14,
        unique=True,
        verbose_name="CPF",
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$',
                message="CPF inválido. Formato esperado: 000.000.000-00."
            )
        ],
        error_messages={
            'blank': "O CPF é obrigatório.",
            'unique': "Este CPF já está cadastrado."
        }
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        error_messages={
            'null': "A Data de Nascimento é obrigatória."
        }
    )

    sexo = models.CharField(
        max_length=1,
        choices=[('M', 'Masculino'), ('F', 'Feminino')],
        verbose_name="Sexo",
        error_messages={
            'blank': "O campo Sexo é obrigatório."
        }
    )

    tipo_sacramento = models.ForeignKey(
        'tipoSacramentos.TipoSacramento',
        on_delete=models.PROTECT,
        verbose_name="TipoSacramento",
        error_messages={
            'null': "O Tipo de Sacramento deve ser selecionado."
        }
    )

    comunidade = models.ForeignKey(
        'comunidades.Comunidade',
        on_delete=models.PROTECT,
        verbose_name="Comunidade",
        error_messages={
            'null': "A Comunidade deve ser selecionada."
        }
    )

    def clean(self):
        super().clean()
        if self.data_nascimento and self.data_nascimento > date.today():
            raise ValidationError({
                'data_nascimento': _("A data de nascimento deve ser no passado.")
            })

    def __str__(self):
        return f"{self.nome} - {self.cpf}"
