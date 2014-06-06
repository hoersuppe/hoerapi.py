from hoerapi.lowlevel import ApiResponse, call_api, parse_date
from hoerapi.CommonEqualityMixin import CommonEqualityMixin


class DeleteEntry(CommonEqualityMixin):
    def __init__(self, data):
        self.event_id = int(data.get('event_ID', None))
        self.deldate = parse_date(data.get('deldate', None))


class DeleteEntryApiResponse(ApiResponse):
    def __init__(self, status, msg, entries):
        ApiResponse.__init__(self, status, msg)

        self.entries = []

        if entries is not None:
            for entry in entries:
                self.entries.append(DeleteEntry(entry))


def get_deleted():
    return call_api('getDeleted', DeleteEntryApiResponse, {})
