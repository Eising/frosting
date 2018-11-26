from frosting.validators import BaseValidator


class IPv6_Address(BaseValidator):

    regular_expression = r'^([A-f0-9:]+:+)+[A-f0-9]+$'
