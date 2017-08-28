from mongoengine import Document, StringField, IntField


class Star(Document):
    name = StringField(required=True, max_length=255)
    rating = IntField()
    dimension = StringField(max_length=255)
