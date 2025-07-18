from dj_rql.filter_cls import AutoRQLFilterClass
from calendarios.models import TipoEvento

class TipoEventoFilterClass(AutoRQLFilterClass):
    MODEL = TipoEvento
