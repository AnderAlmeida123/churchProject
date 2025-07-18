from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf','sexo','data_nascimento')
    search_fields = ('nome','cpf','sexo','data_nascimento')
    list_filter = ('nome','cpf','sexo','data_nascimento')