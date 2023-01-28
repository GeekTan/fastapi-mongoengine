from typing import Iterable, Type

from mongoengine import Document
from pymongo.client_session import ClientSession
from pymongo.collection import Collection
from pymongo.results import InsertOneResult, InsertManyResult


class ExtendCollection:

    def __init__(self, model: Type[Document]):
        self.collection: Collection = getattr(model, "_get_collection")()

    def insert_one(self, document: Document, session: ClientSession) -> InsertOneResult:
        if document:
            document.validate()

            return self.collection.insert_one(document.to_mongo(), session=session)

    def insert_many(self, documents: Iterable[Document], session: ClientSession) -> InsertManyResult:
        for document in documents:
            document: Document
            if document:
                document.validate()
        return self.collection.insert_many([document.to_mongo() for document in documents], session=session)
