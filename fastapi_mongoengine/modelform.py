from typing import Union, Type

import mongoengine
from fastapi.params import Form


class ModelForm(Form):
    model_class: Type[Union[mongoengine.Document, mongoengine.DynamicDocument]]

    def __init__(self, formdata=Form, **kwargs):
        self.instance = kwargs.pop("instance", None) or kwargs.get("obj")
        if self.instance and not formdata:
            kwargs["obj"] = self.instance
        self.formdata = formdata
        super(ModelForm, self).__init__(formdata, **kwargs)

    def save(self, commit=True, **kwargs):
        if not self.instance:
            self.instance = self.model_class()
        self.populate_obj(self.instance)

        if commit:
            self.instance.save(**kwargs)
        return self.instance
