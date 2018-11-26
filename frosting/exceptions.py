class FieldInputNotValid(Exception):
    """The input did not validate according to the validator regex"""
    pass


class InvalidValidatorModule(Exception):
    """Invalid validator specified"""
    pass


class MissingInput(Exception):
    """No input passed, but input is required"""
    pass


class NoStructureLoaded(Exception):
    """No structure has been loaded yet."""
    pass


class UnknownVariable(Exception):
    """No variable by this name."""
    pass


class UnknownOrIncorrectType(Exception):
    """The type is either wrong or undefined"""
    pass


class TemplateCompileError(Exception):
    """Template could not be compiled"""
