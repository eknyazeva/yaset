
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class UnknownTokenAlreadyExists(Error):

    def __init__(self, message):
        self.message = message


class TrainDevInconsistency(Error):

    def __init__(self, message):
        self.message = message
