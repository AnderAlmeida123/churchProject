from dj_rql.filter_cls import AutoRQLFilterClass
from contatos.models import Contato


class ContatoFilterClass(AutoRQLFilterClass):
    MODEL = Contato