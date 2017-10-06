import jsl
from snactor.registry.schemas import registered_schema


class RedHatSignedPackage(jsl.Document):
    name = jsl.StringField()
    vendor = jsl.StringField()
    signature = jsl.StringField()


@registered_schema('1.0')
class RedHatSignedPackages(jsl.Document):
    entries = jsl.ArrayField(jsl.DocumentField(RedHatSignedPackage()))
