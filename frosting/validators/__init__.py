# Define your validator classes here
from frosting.validators.base import BaseValidator
from frosting.validators.ipv4_address import IPv4_Address
from frosting.validators.ipv6_address import IPv6_Address

__all__ = ['IPv4_Address', 'IPv6_Address', 'BaseValidator']

VALIDATORS = [
    {'validators.IPv4_Address': 'Validates IPv4 Addresses, e.g. 10.0.0.1'},
    {'validators.IPv6_Address': 'Validates IPv6 Addresses, e.g. 2001:db8::f00'}
]
