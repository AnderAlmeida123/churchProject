from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Comunidade


class ComunidadeFilterClass(AutoRQLFilterClass):
    MODEL = Comunidade
