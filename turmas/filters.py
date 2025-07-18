from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Turma


class TurmaFilterClass(AutoRQLFilterClass):
    MODEL = Turma
