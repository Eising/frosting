class FieldInputNotValid(Exception):
    """The input did not validate according to the validator regex"""
    pass


class InvalidValidatorModule(Exception):
    """Invalid validator specified"""
    pass


class MissingInput(Exception):
    """No input passed, but input is required"""
    pass
