from frosting.exceptions import MissingInput


class BaseType(object):

    requires_input = False

    def __init__(self, **kwargs):
        if self.requires_input:
            if 'input' in kwargs:
                self.input = kwargs.get('input')
            else:
                raise MissingInput('Missing input')

    def __str__(self):
        pass
