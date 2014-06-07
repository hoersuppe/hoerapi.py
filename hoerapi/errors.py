class HoerApiError(Exception):
    pass


class InvalidJsonError(HoerApiError):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return repr(self.text)


class ApiError(HoerApiError):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)


class NoDataError(HoerApiError):
    pass


class InvalidDataError(HoerApiError):
    def __init__(self, err):
        self.err = err
    def __str__(self):
        return repr(self.err)


class MissingAttributeError(InvalidDataError):
    def __init__(self, attr):
        self.attr = attr
    def __str__(self):
        return repr(self.attr)
