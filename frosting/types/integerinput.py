from frosting.types import BaseType
from frosting.exceptions import FieldInputNotValid
import re
from pprint import pprint


class IntegerInput(BaseType):

    requires_input = True

    def __init__(self, **kwargs):
        """Loads the integer type class. Optional range object can be supplied as
range="""
        pprint(kwargs)
        if "limit" in kwargs:
            limit = kwargs.get('limit')
            regex = re.compile(r'^(\d+)..(\d+)$')
            res = regex.fullmatch(limit)
            if res is not None:
                self.limit = range(int(res.group(1)), int(res.group(2)))
            else:
                raise FieldInputNotValid(
                    "Range expression is invalid. Must be start..end")
        else:
            self.limit = None

        super().__init__(**kwargs)

    def filter(self):
        """ This function also checks if it's actually a number """
        if self.input.__class__ == 'str':
            if self.input.isnumeric():
                self.input = int(self.input)
            else:
                raise FieldInputNotValid("Input is a non-numeric string")

        if self.limit:
            if self.input in self.limit:
                return True
            else:
                return False
        else:
            return True

    def get(self):
        """ Returns the input as integer unless it didn't validate"""
        if self.filter():
            return self.input
        else:
            raise FieldInputNotValid(
                "{} not within {}".format(self.input, self.limit))

    def __str__(self):
        return str(self.get())
