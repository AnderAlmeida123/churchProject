# dizimos/admin.py
from django.contrib import admin
from .models import Dizimo
from .forms import DizimoAdminForm


@admin.register(Dizimo)
class DizimoAdmin(admin.ModelAdmin):
    form = DizimoAdminForm
    list_display = ('id', 'mes', 'tipo_pagamento', 'valor_formatado', 'pessoa')
    search_fields = ('pessoa__nome', 'mes', 'tipo_pagamento', 'responsavel__username')
    list_filter = ('pessoa', 'mes', 'tipo_pagamento', 'responsavel')

    def valor_formatado(self, obj):
        return f"R$ {obj.valor:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.')

    valor_formatado.short_description = "Valor"
