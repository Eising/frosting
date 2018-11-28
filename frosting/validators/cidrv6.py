from frosting.validators import BaseValidator


class CIDRv6(BaseValidator):
    """ Validates CIDRv6 addresses """

    regular_expression = r'^([A-f0-9:]+:+)+[A-f0-9]+\/[0-9]+$'
