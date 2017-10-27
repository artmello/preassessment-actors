import jsl
from snactor.registry.schemas import registered_schema


@registered_schema('1.0')
class StringList(jsl.Document):
    list = jsl.ArrayField(jsl.StringField())
