from dj_rql.filter_cls import AutoRQLFilterClass
from calendarios.models import Calendario

class CalendarioFilterClass(AutoRQLFilterClass):
    MODEL = Calendario
