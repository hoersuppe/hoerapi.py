from datetime import datetime
from pytz import timezone


''' zone for time returned by API '''
DefaultZone = timezone('Europe/Berlin')
def parse_date(val):
    val = datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
    return DefaultZone.localize(val)


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