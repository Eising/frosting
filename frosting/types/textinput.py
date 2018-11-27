from frosting.types import BaseType
import importlib
from frosting.exceptions import InvalidValidatorModule, FieldInputNotValid


class TextInput(BaseType):

    requires_input = True
    ALLOWED_INCLUDE_PATH = ['frosting.']

    def __init__(self, **kwargs):
        """Fetches the validator from the input kwargs, and initiates the parent
        class"""
        if "validator" in kwargs and len(kwargs.get('validator')) > 0:
            self.validator = kwargs.get('validator')
        else:
            self.validator = None

        # TODO: Allow modification of ALLOWED_INCLUDE_PATH

        super().__init__(**kwargs)

    def filter(self):
        """
        Filter loads the validator dynamically, and validates the text input.
        """
        if self.validator is not None:
            try:
                for allowed_module in self.ALLOWED_INCLUDE_PATH:
                    if not self.validator.startswith(allowed_module):
                        raise InvalidValidatorModule(
                            "Validator refers to a module not explicitly allowed")

                validator_module = self.validator.split(".")
                validator_class = validator_module.pop()
                validator_module_path = ".".join(validator_module)
                validators = importlib.import_module(validator_module_path)

                if hasattr(validators, validator_class):
                    validator = getattr(validators, validator_class)
                else:
                    raise InvalidValidatorModule(
                        "Invalid validator {}".format(validator_class))
            except ModuleNotFoundError:
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
