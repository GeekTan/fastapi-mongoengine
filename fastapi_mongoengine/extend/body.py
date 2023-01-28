from typing import Type

from mongoengine import Document
from pydantic import BaseModel


class JsonBody:
    db_model: Type[Document]
    pydantic_model: BaseModel

    def __init__(self, db_model: Type[Document], pydantic_model: BaseModel):
        self.db_model = db_model
        self.pydantic_model = pydantic_model

    # TODO 对pydantic_model和db_model模型进行匹配
    def save(self):
        self.db_model(**self.pydantic_model.dict()).save()
