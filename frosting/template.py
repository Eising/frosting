import pystache
import pyaml
import json


class FrostingTemplate:

    DEFAULT_VAR_TYPE = "types.TextInput"

    def __init__(self, template):
        self.template = template

    def template_tags(self):
        parsed_template = pystache.parse(self.template)
        keys = []
        parse_tree = parsed_template._parse_tree
        keyed_classes = (pystache.parser._EscapeNode,
                         pystache.parser._LiteralNode,
                         pystache.parser._InvertedNode,
                         pystache.parser._SectionNode)
        for token in parse_tree:
            if isinstance(token, keyed_classes):
                keys.append(token.key)
        # return list of unique items
        # (json does not like sets)
        return list(set(keys))

    def service_structure(self):
        builder = {'name': '', 'vars': {}}

        for tag in self.template_tags():
            builder['vars'][tag] = {
                'type': self.DEFAULT_VAR_TYPE, 'validator': ''}

        return builder

    def yaml_dump(self):
        return pyaml.dump(self.service_structure())

    def json_dump(self):
        return json.dumps(self.service_structure())
