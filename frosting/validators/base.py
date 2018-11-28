import re


class BaseValidator(object):

    def __init__(self, **kwargs):
        # Do nothing
        pass

    regular_expression = None
    valid_range = None

    def validate(self, input):
        if self.regular_expression is not None:
            validator = re.compile(self.regular_expression)
            result = validator.fullmatch(input)

            if result:
                return True
            else:
                return False
        elif self.valid_range is not None:
            if type(input) is str:
                if not input.isnumeric():
                    return False
            if int(input) in self.valid_range:
                return True
            else:
                return False
        else:
            # Nothing to validate
            return True
