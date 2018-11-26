from frosting.types import BaseType
import importlib
from frosting.exceptions import InvalidValidatorModule, FieldInputNotValid


class TextInput(BaseType):

    requires_input = True

    def __init__(self, **kwargs):
        self.validator = kwargs.get('validator')
        super().__init__(**kwargs)

    def filter(self):
        try:
            validators = importlib.import_module('frosting.validators')
            if hasattr(validators, self.validator):
                validator = getattr(validators, self.validator)
            else:
                raise InvalidValidatorModule("Invalid validator")
        except importlib.ModuleNotFoundError:
            raise InvalidValidatorModule("Invalid validator")

        if hasattr(validator, "validate"):
            tvalidator = validator()
            return tvalidator.validate(self.input)
        else:
            raise InvalidValidatorModule("Invalid validator")

    def __str__(self):
        if self.filter():
            return str(self.input)
        else:
            raise FieldInputNotValid(
                "{} is not a valid {}".format(self.input, self.validator))
