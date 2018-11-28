# Define your validator classes here
from frosting.validators.base import BaseValidator
from frosting.validators.ipv4_address import IPv4_Address
from frosting.validators.ipv6_address import IPv6_Address
from frosting.validators.regex_validator import RegexValidator
from frosting.validators.asn import ASN
from frosting.validators.vlan import VLAN
from frosting.validators.iosxr_physical_interface import IOSXR_Physical_Interface
from frosting.validators.cidrv4 import CIDRv4
from frosting.validators.cidrv6 import CIDRv6

__all__ = ['IPv4_Address', 'IPv6_Address',
           'BaseValidator', 'RegexValidator', 'ASN', 'VLAN', 'IOSXR_Physical_Interface', 'CIDRv4', 'CIDRv6']

VALIDATORS = [
    {'frosting.validators.IPv4_Address': 'Validates IPv4 Addresses, e.g. 10.0.0.1'},
    {'frosting.validators.CIDRv4': 'Validates IPv4 prefixes, e.g. 10.0.0.1/32'},
    {'frosting.validators.IPv6_Address': 'Validates IPv6 Addresses, e.g. 2001:db8::f00'},
    {'frosting.validators.CIDRv6': 'Validates IPv6 prefixes, e.g. 2001:db8::f00/64'},
    {'frosting.validators.RegexValidator': 'A generic Regex validator. Specify \'regex: \''},
    {'frosting.validators.ASN': 'Validates AS-numbers'},
    {'frosting.validators.VLAN': 'Validates VLAN-numbers'},
    {'frosting.validators.IOSXR_Physical_Interface': 'Validates physical IOS-XR interfaces'}

]
