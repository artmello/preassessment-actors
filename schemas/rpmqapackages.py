import jsl


class RPMQAPackage(jsl.Document):
    name = jsl.StringField()
    vendor = jsl.StringField()
    signature = jsl.StringField()


class RPMQAPackages(jsl.Document):
    entries = jsl.ArrayField(jsl.DocumentField(RPMQAPackage()))
