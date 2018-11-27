from frosting.exceptions import NoStructureLoaded, UnknownVariable, UnknownOrIncorrectType, TemplateCompileError
from frosting.template import FrostingTemplate
from ruamel.yaml import YAML
import importlib
import re
from pprint import pprint


class Frosting(object):
    # require all function filters to start with 'frosting.'
    ALLOWED_INCLUDE_PATH = ['frosting.']

    def __init__(self, template, **kwargs):
        self.template = FrostingTemplate(template)
        self.input = {}
        self.structure = None
        if 'allowed_modules' in kwargs:
            modules = kwargs.get('allowed_modules')
            if modules.__class__ == 'list':
                for omodule in modules:
                    self.ALLOWED_INCLUDE_PATH.append(omodule)
            else:
                self.ALLOWED_INCLUDE_PATH.append(modules)

    def load_yaml_structure(self, structure):
        yaml = YAML()
        self.structure = yaml.load(structure)

    def add(self, variable, contents):
        """Collect a variable and its input, validate"""
        if self.structure is None:
            # There is no structure loaded
            raise NoStructureLoaded
        if variable in self.structure['vars']:
            # The variable exists in the structure
            # Extract the type
            for allowed_type in self.ALLOWED_INCLUDE_PATH:
                if not self.structure['vars'][variable]['type'].startswith(allowed_type):
                    raise UnknownOrIncorrectType(
                        "Type refers to a module not explicitly allowed")

            typepath = self.structure['vars'][variable]['type'].split(
                ".")  # Split the object path
            classname = typepath.pop()  # Get the rightmost name
            try:
                frostmod = importlib.import_module(".".join(typepath))
                if hasattr(frostmod, classname):
                    frosttype = getattr(frostmod, classname)
                    if frosttype.requires_input:
                        inputs = frosttype(
                            input=contents, **self.structure['vars'][variable])
                        self.input[variable] = inputs.get()

                    else:
                        # We still want to pass variables
                        inputs = frosttype(**self.structure['vars'][variable])
                        self.input[variable] = inputs.get()
                else:
                    raise UnknownOrIncorrectType(
                        "The type class doesn't exist")
            except ModuleNotFoundError:
                raise UnknownOrIncorrectType("Couldn't load the module")

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
