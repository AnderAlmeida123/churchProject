from django.contrib import admin
from .forms import CalendarioAdminForm
from .models import Calendario


@admin.register(Calendario)
class CalendarioAdmin(admin.ModelAdmin):
    form = CalendarioAdminForm
    list_display = ('id','titulo_evento', 'data_hora', 'comunidade', 'tipo_evento', 'criado_em','atualizado_em')
    search_fields = ('titulo_evento', 'descricao')
    list_filter = ('data_hora', 'comunidade__nome_comunidade', 'tipo_evento__nome_Evento')
