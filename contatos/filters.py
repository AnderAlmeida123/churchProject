from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Contato


class ContatoFilterClass(AutoRQLFilterClass):
    MODEL = Contato