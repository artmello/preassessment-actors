import jsl


class ChkconfigList(jsl.Document):
    entries = jsl.ArrayField(jsl.StringField())
