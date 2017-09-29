import jsl


class RedHatSignedPackage(jsl.Document):
    name = jsl.StringField()
    vendor = jsl.StringField()
    signature = jsl.StringField()


class RedHatSignedPackages(jsl.Document):
    entries = jsl.ArrayField(jsl.DocumentField(RedHatSignedPackage()))
