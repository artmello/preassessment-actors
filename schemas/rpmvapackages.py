import jsl


class RPMVAPackages(jsl.Document):
    entries = jsl.ArrayField(jsl.StringField())
