from dj_rql.filter_cls import AutoRQLFilterClass
from dizimos.models import Dizimo


class DizimoFilterClass(AutoRQLFilterClass):
    MODEL = Dizimo
