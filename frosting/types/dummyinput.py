from frosting.types import BaseType


class DummyInput(BaseType):
    """ This just passes input to get() and __str__ """

    requires_input = True

    def get(self):
        return self.input

    def __str__(self):
        return str(self.get())
