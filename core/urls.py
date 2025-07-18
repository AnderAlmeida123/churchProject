from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Schema gerado automaticamente
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Documentação interativa com Swagger
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Documentação estilo Redoc
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Seus apps versionados
    path('api/v1/calendarios/', include('calendarios.urls')),
    path('api/v1/comunidades/', include('comunidades.urls')),
    path('api/v1/contatos/', include('contatos.urls')),
    path('api/v1/dizimos/', include('dizimos.urls')),
    path('api/v1/enderecos/', include('enderecos.urls')),
    path('api/v1/membroSetores/', include('membroSetores.urls')),
    path('api/v1/membroTurmas/', include('membroTurmas.urls')),
    path('api/v1/movimentacaoProdutos/', include('movimentacaoProdutos.urls')),
    path('api/v1/pessoas/', include('pessoas.urls')),
    path('api/v1/produtos/', include('produtos.urls')),
    path('api/v1/sacramentos/', include('sacramentos.urls')),
    path('api/v1/setores/', include('setores.urls')),
    path('api/v1/tesouraria/', include('tesouraria.urls')),
    path('api/v1/tipoEventos/', include('tipoEventos.urls')),
    path('api/v1/tipoSacramentos/', include('tipoSacramentos.urls')),
    path('api/v1/turmas/', include('turmas.urls')),

    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rota para raiz do site
    path('', lambda request: JsonResponse({
        "message": "Bem-vindo à API do Church System",
        "documentacao": "/api/v1/docs/",
        "admin": "/admin/"
    })),
]
