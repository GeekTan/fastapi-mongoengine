from typing import Iterable, Type, Mapping, Any, Optional

from mongoengine import Document
from pymongo.client_session import ClientSession
from pymongo.collection import Collection, ReturnDocument
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

    def replace_one(self,
                    filter: Mapping[str, Any],
                    replacement: Mapping[str, Any],
                    upsert=False,
                    bypass_document_validation=False,
                    collation=None,
                    hint=None,
                    session=None,
                    let=None,
                    comment=None):
        return self.collection.replace_one(filter, replacement, upsert, bypass_document_validation, collation, hint,
                                           session, let, comment)

    def update_one(self,
                   filter: Mapping[str, Any],
                   update,
                   upsert=False,
                   bypass_document_validation=False,
                   collation=None,
                   array_filters=None,
                   hint=None,
                   session=None,
                   let=None,
                   comment=None,
                   ):
        return self.collection.update_one(filter, update, upsert, bypass_document_validation, collation, array_filters,
                                          hint, session, let, comment)

    def update_many(self,
                    filter: Mapping[str, Any],
                    update,
                    upsert=False,
                    array_filters=None,
                    bypass_document_validation=None,
                    collation=None,
                    hint=None,
                    session=None,
                    let=None,
                    comment=None,
                    ):
        return self.collection.update_many(filter, update, upsert, array_filters, bypass_document_validation, collation,
                                           hint, session, let, comment)

    def delete_one(self,
                   filter: Mapping[str, Any],
                   collation=None,
                   hint=None,
                   session=None,
                   let=None,
                   comment=None,
                   ):
        return self.collection.delete_one(filter, collation, hint, session, let, comment)

    def delete_many(self,
                    filter: Mapping[str, Any],
                    collation=None,
                    hint=None,
                    session=None,
                    let=None,
                    comment=None,
                    ):
        return self.collection.delete_many(filter, collation, hint, session, let, comment)

    def find_one(self,
                 filter: Optional[Any] = None,
                 *args: Any,
                 **kwargs: Any,
                 ):
        return self.collection.find_one(filter, *args, **kwargs)

    def find(self,
             filter: Optional[Any] = None,
             *args: Any,
             **kwargs: Any,
             ):
        return self.collection.find(filter, *args, **kwargs)

    def find_raw_batches(self, *args: Any, **kwargs: Any):
        return self.collection.find_raw_batches(*args, **kwargs)

    def estimated_document_count(self, comment: Optional[Any] = None, **kwargs: Any):
        return self.collection.estimated_document_count(comment, **kwargs)

    def count_documents(self,
                        filter: Mapping[str, Any],
                        session: Optional[ClientSession] = None,
                        comment: Optional[Any] = None,
                        **kwargs: Any,
                        ):
        return self.collection.count_documents(filter, session, comment, **kwargs)

    def aggregate(self,
                  pipeline,
                  session: Optional[ClientSession] = None,
                  let: Optional[Mapping[str, Any]] = None,
                  comment: Optional[Any] = None,
                  **kwargs: Any,
                  ):
        return self.collection.aggregate(pipeline, session, let, comment, **kwargs)

    def aggregate_raw_batches(self,
                              pipeline,
                              session: Optional["ClientSession"] = None,
                              comment: Optional[Any] = None,
                              **kwargs: Any,
                              ):
        return self.collection.aggregate_raw_batches(pipeline, session, comment, **kwargs)

    def distinct(self,
                 key: str,
                 filter: Optional[Mapping[str, Any]] = None,
                 session: Optional[ClientSession] = None,
                 comment: Optional[Any] = None,
                 **kwargs: Any,
                 ):
        return self.collection.distinct(key, filter, session, comment, **kwargs)

    def find_one_and_delete(self,
                            filter: Mapping[str, Any],
                            projection=None,
                            sort=None,
                            hint=None,
                            session: Optional[ClientSession] = None,
                            let: Optional[Mapping[str, Any]] = None,
                            comment: Optional[Any] = None,
                            **kwargs: Any,
                            ):
        return self.collection.find_one_and_delete(filter, projection, sort, hint, session, let, comment, **kwargs)

    def find_one_and_replace(self,
                             filter: Mapping[str, Any],
                             replacement: Mapping[str, Any],
                             projection=None,
                             sort=None,
                             upsert: bool = False,
                             return_document=ReturnDocument.BEFORE,
                             hint=None,
                             session: Optional[ClientSession] = None,
                             let: Optional[Mapping[str, Any]] = None,
                             comment: Optional[Any] = None,
                             **kwargs: Any,
                             ):
        return self.collection.find_one_and_replace(filter, replacement, projection, sort, upsert, return_document,
                                                    hint, session, let, comment, **kwargs)

    def find_one_and_update(self,
                            filter: Mapping[str, Any],
                            update,
                            projection=None,
                            sort=None,
                            upsert: bool = False,
                            return_document: bool = ReturnDocument.BEFORE,
                            array_filters=None,
                            hint=None,
                            session: Optional[ClientSession] = None,
                            let: Optional[Mapping[str, Any]] = None,
                            comment: Optional[Any] = None,
                            **kwargs: Any,
                            ):
        return self.collection.find_one_and_update(filter, update, projection, sort, upsert, return_document,
                                                   array_filters, hint, session, let, comment, **kwargs)
