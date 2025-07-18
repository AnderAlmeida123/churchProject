from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Pessoa


class PessoaFilterClass(AutoRQLFilterClass):
    MODEL = Pessoa