from frosting.validators import BaseValidator


class CIDRv4(BaseValidator):
    """ Validates CIDRv4 addresses """

    regular_expression = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/[0-9]+$'
