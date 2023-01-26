import mongoengine

from fastapi_mongoengine.extend.queryset import ExtendQuerySet


class ExtendDocument(mongoengine.Document):
    meta = {"queryset_class": ExtendQuerySet}


class ExtendDynamicDocument(mongoengine.DynamicDocument):
    meta = {"queryset_class": ExtendQuerySet}
