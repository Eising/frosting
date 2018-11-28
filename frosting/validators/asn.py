from frosting.validators import BaseValidator


class ASN(BaseValidator):
    """ Validate AS numbers, including 4byte ASN """

    valid_range = range(1, 4294967296)
