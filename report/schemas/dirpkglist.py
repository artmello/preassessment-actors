import jsl
from snactor.registry.schemas import registered_schema


@registered_schema('1.0')
class DirPkgField(jsl.Document):
    dir = jsl.StringField(required=True)
    pkg = jsl.StringField(required=True)


@registered_schema('1.0')
class DirPkgList(jsl.Document):
    list = jsl.ArrayField(jsl.DocumentField(DirPkgField, as_ref=True))
