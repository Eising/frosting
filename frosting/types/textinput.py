from frosting.types import BaseType
import importlib
from frosting.exceptions import InvalidValidatorModule, FieldInputNotValid


class TextInput(BaseType):

    requires_input = True

    def __init__(self, **kwargs):
        """Fetches the validator from the input kwargs, and initiates the parent
        class"""
        if "validator" in kwargs and len(kwargs.get('validator')) > 0:
            self.validator = kwargs.get('validator')
        else:
            self.validator = None

        super().__init__(**kwargs)

    def filter(self):
        """
        Filter loads the validator dynamically, and validates the text input.
        """
        if self.validator is not None:
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
        else:
            return True

    def get(self):
        """ Returns the input as string unless it did not validate """
        if self.filter():
            return self.input
        else:
            raise FieldInputNotValid(
                "{} is not a valid {}".format(self.input, self.validator))

    def __str__(self):
        return str(self.get())
