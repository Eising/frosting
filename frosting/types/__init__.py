# Define your type classes here
from frosting.types.base import BaseType
from frosting.types.textinput import TextInput
from frosting.types.integerinput import IntegerInput

__all__ = ['BaseType', 'TextInput', 'IntegerInput']

TYPES = [
    {'types.TextInput': 'String input, supports validator parameter'},
    {'types.IntegerInput': 'Number input, supports limit parameter'}
]
