import unittest
from frosting import Frosting
import frosting.exceptions


class TestTemplates(unittest.TestCase):
    def setUp(self):
        self.template = "{{var1}}:{{var2}}"
        self.structure = """---
vars:
    var1:
        type: frosting.types.TextInput
        validator: "frosting.validators.IPv4_Address"
    var2:
        type: frosting.types.TextInput
        validator: "frosting.validators.IPv4_Address" """

    def test_template_no_structure(self):
        frosting = Frosting(self.template)
        frosting.add("var1", "foo")
        frosting.add("var2", "bar")
        result = frosting.compile()
        self.assertEqual(result, "foo:bar")

    def test_template_with_structure(self):
        frosting = Frosting(self.template)
        frosting.load_yaml_structure(self.structure)
        frosting.add("var1", "1.1.1.1")
        frosting.add("var2", "2.2.2.2")
        result = frosting.compile()

        self.assertEqual(result, "1.1.1.1:2.2.2.2")

    def test_validator(self):
        frost = Frosting(self.template)
        frost.load_yaml_structure(self.structure)
        with self.assertRaises(frosting.exceptions.FieldInputNotValid):
            frost.add("var1", "1.1.1.1.1")

    def test_dict_structure(self):
        frost = Frosting(self.template)
        structure = {
            "var1": {
                'type': 'frosting.types.TextInput',
                'validator': 'frosting.validators.IPv4_Address'},
            "var2": {
                'type': 'frosting.types.TextInput',
                'validator': 'frosting.validators.IPv4_Address'}
        }
        frost.load_structure(structure)
        frost.add("var1", "1.1.1.1")
        frost.add("var2", "2.2.2.2")
        result = frost.compile()

        self.assertEqual(result, "1.1.1.1:2.2.2.2")

    def test_limit1(self):
        frost = Frosting(self.template)
        structure = {
            "var1": {
                'type': 'frosting.types.TextInput',
                'validator': 'frosting.validators.IPv4_Address'},
            "var2": {
                'type': 'frosting.types.IntegerInput',
                'limit': '1..100'}
        }
        frost.load_structure(structure)
        frost.add("var1", "1.1.1.1")
        frost.add("var2", 99)
        result = frost.compile()

        self.assertEqual(result, "1.1.1.1:99")

    def test_limit_string_input(self):
        frost = Frosting(self.template)
        structure = {
            "var1": {
                'type': 'frosting.types.TextInput',
                'validator': 'frosting.validators.IPv4_Address'},
            "var2": {
                'type': 'frosting.types.IntegerInput',
                'limit': '1..100'}
        }
        frost.load_structure(structure)
        frost.add("var1", "1.1.1.1")
        frost.add("var2", "99")
        result = frost.compile()

        self.assertEqual(result, "1.1.1.1:99")


if __name__ == '__main__':
    unittest.main()
