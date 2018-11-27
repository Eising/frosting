# Define your type classes here
from frosting.types.base import BaseType
from frosting.types.textinput import TextInput
from frosting.types.integerinput import IntegerInput
from frosting.types.dummyinput import DummyInput

__all__ = ['BaseType', 'TextInput', 'IntegerInput', 'DummyInput']

TYPES = [
    {'frosting.types.DummyInput', 'Passes input as output raw'},
    {'frosting.types.TextInput': 'String input, supports validator parameter'},
    {'frositng.types.IntegerInput': 'Number input, supports limit parameter'}
]
