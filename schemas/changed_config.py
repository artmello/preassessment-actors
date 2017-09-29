import jsl


class ChangedConfig(jsl.Document):
    entries = jsl.ArrayField(jsl.StringField())
