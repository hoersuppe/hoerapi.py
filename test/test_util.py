import pytest
from hoerapi.util import parse_bool, parse_date
from datetime import datetime


def test_parse_date():
    assert parse_date('2012-12-02 13:00:00') == datetime(2012, 12, 2, 13, 0, 0)


@pytest.mark.parametrize("str,bool", [
    ('', False),
    ('0', False),
    ('1', True),
    ('invalid22', False),
])
def test_parse_bool(str, bool):
    assert parse_bool(str) == bool