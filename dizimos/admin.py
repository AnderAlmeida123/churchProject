from django.contrib import admin
from .models import Dizimo
from .forms import DizimoAdminForm


@admin.register(Dizimo)
class DizimoAdmin(admin.ModelAdmin):
    form = DizimoAdminForm

    list_display = (
        'id',
        'mes',
        'tipo_pagamento',
        'valor_formatado',
        'pessoa',
        'responsavel',
        'criado_em'
    )

    search_fields = (
        'pessoa__nome',
        'mes',
        'tipo_pagamento',
        'responsavel__username'
    )

    list_filter = (
        'mes',
        'tipo_pagamento',
        'pessoa',
        'responsavel'
    )

    ordering = ('-criado_em',)

    def valor_formatado(self, obj):
        return f"R$ {obj.valor:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.')

    valor_formatado.short_description = "Valor"
    valor_formatado.admin_order_field = 'valor'
