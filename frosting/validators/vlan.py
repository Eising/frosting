from frosting.validators import BaseValidator


class VLAN(BaseValidator):
    """ Validates VLANs """

    valid_range = range(1, 4094)
