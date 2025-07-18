from dj_rql.filter_cls import AutoRQLFilterClass
from .models import MembroTurma


class MembroTurmaFilterClass(AutoRQLFilterClass):
    MODEL = MembroTurma