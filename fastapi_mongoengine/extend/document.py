from mongoengine import DynamicDocument, Document

from fastapi_mongoengine.extend.queryset import ExtendQuerySet


class ExtendDocument(Document):
    meta = {"queryset_class": ExtendQuerySet, "abstract": True}


class ExtendDynamicDocument(DynamicDocument):
    meta = {"queryset_class": ExtendQuerySet, "abstract": True}
