from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Tesouraria


class TesourariaFilter(AutoRQLFilterClass):
    class Meta:
        model = Tesouraria