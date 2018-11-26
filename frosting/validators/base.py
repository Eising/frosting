import re


class BaseValidator(object):

    regular_expression = r'.*'

    def validate(self, input):
        validator = re.compile(self.regular_expression)
        result = validator.fullmatch(input)

        if result:
            return True
        else:
            return False
