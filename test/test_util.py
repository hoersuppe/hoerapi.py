import pytest
from hoerapi.util import parse_bool, parse_date, DefaultZone
from datetime import datetime
from iso8601 import UTC

def test_parse_date():
    local = DefaultZone.localize(datetime(2012, 12, 2, 13, 0, 0))
    utc   = datetime(2012, 12, 2, 13, 0, 0, tzinfo=UTC)
    assert parse_date('2012-12-02 13:00:00') == local
    assert parse_date('2012-12-02T13:00:00') == local
    assert parse_date('2012-12-02T13:00:00Z') == utc


@pytest.mark.parametrize("str,bool", [
    ('', False),
    ('0', False),
    ('1', True),
    ('invalid22', False),
])
def test_parse_bool(str, bool):
    assert parse_bool(str) == bool