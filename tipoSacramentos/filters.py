from dj_rql.filter_cls import AutoRQLFilterClass
from .models import TipoSacramento

class TipoSacramentoFilterClass(AutoRQLFilterClass):
    MODEL = TipoSacramento
