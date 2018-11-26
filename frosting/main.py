from frosting.exceptions import NoStructureLoaded, FieldInputNotValid, UnknownVariable, UnknownOrIncorrectType, TemplateCompileError
from frosting.template import FrostingTemplate
from ruamel.yaml import YAML
import importlib
import re
from pprint import pprint


class Frosting(object):

    def __init__(self, template):
        self.template = FrostingTemplate(template)
        self.input = {}
        self.structure = None

    def load_yaml_structure(self, structure):
        yaml = YAML()
        self.structure = yaml.load(structure)

    def add(self, variable, contents):
        """Collect a variable and its input, validate"""
        if self.structure is None:
            # There is no structure loaded
            raise NoStructureLoaded
        if variable in self.structure['vars'] and self.structure['vars'][variable]['type'].startswith('types.'):
            # The variable exists in the structure
            regex = re.compile(r'^types\.(.+)$')
            typename = regex.fullmatch(
                self.structure['vars'][variable]['type']).group(1)
            try:
                types = importlib.import_module('frosting.types')
                if hasattr(types, typename):
                    typedef = getattr(types, typename)
                    if typedef.requires_input is False:
                        inputs = typedef()
                        self.input[variable] = inputs.get()
                    else:
                        if "validator" in self.structure['vars'][variable] and len(self.structure['vars'][variable]['validator']) > 0:
                            regex = re.compile(r'^validators\.(.+)$')
                            validator = regex.fullmatch(
                                self.structure['vars'][variable]['validator']).group(1)
                            validated = typedef(
                                validator=validator, input=contents)
                            self.input[variable] = validated.get()
                        else:
                            pprint(self.structure['vars'][variable])
                            unvalidated = typedef(
                                input=contents, **self.structure['vars'][variable])
                            self.input[variable] = unvalidated.get()

                else:
                    raise UnknownOrIncorrectType(
                        "The type class doesn't exist")
            except ModuleNotFoundError:
                raise UnknownOrIncorrectType("Invalid type definition")

        else:
            raise UnknownVariable("The variable was not recogniced")

    def compile(self):
        """ Compile the template"""
        # First check if all inputs are set

        tags = self.template.template_tags()
        vars = list(self.input.keys())
        tags.sort()
        vars.sort()

        if vars == tags:
            return self.template.compile_template(**self.input)
        else:
            raise TemplateCompileError(
                "Template could not be compiled due to missing variables")
