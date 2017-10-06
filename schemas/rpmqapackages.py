import jsl
from snactor.registry.schemas import registered_schema


class RPMQAPackage(jsl.Document):
    name = jsl.StringField()
    vendor = jsl.StringField()
    signature = jsl.StringField()


@registered_schema('1.0')
class RPMQAPackages(jsl.Document):
    entries = jsl.ArrayField(jsl.DocumentField(RPMQAPackage()))
