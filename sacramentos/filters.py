from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Sacramento


class SacramentoFilterClass(AutoRQLFilterClass):
    MODEL = Sacramento
