from django.contrib import admin
from enderecos.models import Endereco
from .forms import EnderecoAdminForm


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    form = EnderecoAdminForm
    list_display = ('id', 'cep_formatado', 'estado', 'cidade', 'bairro', 'rua', 'numero', 'referencia', 'atualizado_em',
                    'criado_em', 'responsavel', 'pessoa')
    search_fields = ['cep', 'rua', 'pessoa__user__first_name']
    list_filter = ('cep', 'rua', 'pessoa','bairro')
