from frosting.validators import BaseValidator


class IOSXR_Physical_Interface(BaseValidator):
    """ Validates Physical interfaces on IOSXR """

    regular_expression = r'^(?:FastEthernet|GigabitEthernet|TenGigE|FortyGigE|HundredGigE|Serial|POS)(?:[0-9+]\/)+(?:[0-9])$'
