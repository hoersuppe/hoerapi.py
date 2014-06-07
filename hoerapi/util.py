from datetime import datetime


def parse_date(str):
    return datetime.strptime(str, "%Y-%m-%d %H:%M:%S")


def parse_bool(str):
    if str == "1":
        return True
    else:
        return False


class CommonEqualityMixin(object):
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)
    def __ne__(self, other):
        return not self.__eq__(other)