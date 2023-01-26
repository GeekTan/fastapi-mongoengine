from mongoengine import Document, StringField
from pydantic import BaseModel, constr


class User(Document):
    name = StringField(primary_key=True, unique=True, max_length=20)
    phone = StringField(max_length=11)

    meta = {"db_alias": "test_db"}


class UserModel(BaseModel):
    name: constr(max_length=20)
    phone: constr(max_length=11)
