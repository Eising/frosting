from frosting.validators import BaseValidator
import frosting.exceptions
import re


class RegexValidator(BaseValidator):

    def __init__(self, **kwargs):
        if 'regex' in kwargs:
            # Validate regular expression
            regex = kwargs.get('regex')
            try:
                re.compile(regex)
            except re.error:
                raise frosting.exceptions.InvalidValidatorModule(
                    "Regular Expression did not validate")

            self.regular_expression = regex
