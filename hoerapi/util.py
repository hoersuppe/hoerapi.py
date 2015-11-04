from datetime import datetime
from iso8601 import parse_date as parse_isodate
from pytz import timezone


''' zone for time returned by API '''
DefaultZone = timezone('Europe/Berlin')
def parse_date(val):
    val = parse_isodate(val, DefaultZone)
    ''' date has ISO zone information '''
    if val.tzinfo != DefaultZone:
        return val
    ''' fix zoneinfo for obtained time '''
    val = datetime.combine(val.date(), val.time())
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