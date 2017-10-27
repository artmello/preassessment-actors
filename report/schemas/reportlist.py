import jsl
from snactor.registry.schemas import registered_schema


@registered_schema('1.0')
class ReportList(jsl.Document):
    report = jsl.ArrayField(jsl.StringField())
