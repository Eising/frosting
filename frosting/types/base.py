from frosting.exceptions import MissingInput


class BaseType(object):
    """This is the base type class. It implements the 'requires_input' instance
    variable, that controls whether the subclass type should ask for a verbatim
    input"""

    requires_input = False

    def __init__(self, **kwargs):
        if self.requires_input:
            if 'input' in kwargs:
                self.input = kwargs.get('input')
            else:
                raise MissingInput('Missing input')

    def __str__(self):
        pass
