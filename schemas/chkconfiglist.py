import jsl
from snactor.registry.schemas import registered_schema


@registered_schema('1.0')
class ChkconfigList(jsl.Document):
    entries = jsl.ArrayField(jsl.StringField())
