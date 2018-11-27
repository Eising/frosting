# Define your type classes here
from frosting.types.base import BaseType
from frosting.types.textinput import TextInput
from frosting.types.integerinput import IntegerInput

__all__ = ['BaseType', 'TextInput', 'IntegerInput']

TYPES = [
    {'frosting.types.TextInput': 'String input, supports validator parameter'},
    {'frositng.types.IntegerInput': 'Number input, supports limit parameter'}
]
