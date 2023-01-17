from typing import Type, Iterable

from mongoengine import Document
from pymongo.client_session import ClientSession
from pymongo.collection import Collection
from pymongo.results import InsertManyResult, InsertOneResult


class Transaction:
    def __init__(self, model: Type[Document]):
        self.conn: Collection = getattr(model, "_get_collection")

    def insert_one(self, document: Document, session: ClientSession) -> InsertOneResult:
        if document:
            document.validate()
            return self.conn.insert_one(document.to_mongo(), session=session)

    def insert_many(self, documents: Iterable[Document], session: ClientSession) -> InsertManyResult:
        for document in documents:
            document: Document
            if document:
                document.validate()
        return self.conn.insert_many([document.to_mongo() for document in documents], session=session)

    @property
    def conn(self):
        return self.conn
