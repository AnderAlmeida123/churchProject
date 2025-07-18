from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Endereco


class EnderecoFilterClass(AutoRQLFilterClass):
    MODEL = Endereco