# Define your validator classes here
from frosting.validators.base import BaseValidator
from frosting.validators.ipv4_address import IPv4_Address
from frosting.validators.ipv6_address import IPv6_Address
from frosting.validators.regex_validator import RegexValidator
from frosting.validators.asn import ASN

__all__ = ['IPv4_Address', 'IPv6_Address',
           'BaseValidator', 'RegexValidator', 'ASN']

VALIDATORS = [
    {'frosting.validators.IPv4_Address': 'Validates IPv4 Addresses, e.g. 10.0.0.1'},
    {'frosting.validators.IPv6_Address': 'Validates IPv6 Addresses, e.g. 2001:db8::f00'},
    {'frosting.validators.RegexValidator': 'A generic Regex validator. Specify \'regex: \''},
    {'frosting.validators.ASN': 'Validates AS-numbers'}
]
