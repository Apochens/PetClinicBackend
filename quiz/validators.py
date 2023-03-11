from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class JsonFieldValidator:
    message = _("%{field}s not a valid field")

    def __init__(self, fields: list):
        self.fields = fields

    def __call__(self, value: dict, *args, **kwargs):
        for field in value.keys():
            if field not in self.fields:
                raise ValidationError(
                    f"Field <{field}> is not a valid field"
                )
            if not isinstance(value[field], list):
                raise ValidationError(
                    f"Field <{field}> is not a list"
                )
        return

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and (self.fields == other.fields)
        )
