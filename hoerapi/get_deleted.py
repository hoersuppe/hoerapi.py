from hoerapi.lowlevel import call_api
from hoerapi.util import parse_date, CommonEqualityMixin
from hoerapi.parser import parser_list


class DeleteEntry(CommonEqualityMixin):
    def __init__(self, data):
        self.event_id = int(data['event_ID'])
        self.deldate = parse_date(data['deldate'])


def get_deleted(dateStart=None, dateEnd=None):
    params = {}

    if dateStart is not None:
        params['dateStart'] = dateStart.strftime('%y-%m-%d')
    if dateEnd is not None:
        params['dateEnd'] = dateEnd.strftime('%y-%m-%d')

    return parser_list(DeleteEntry, call_api('getDeleted', params))
