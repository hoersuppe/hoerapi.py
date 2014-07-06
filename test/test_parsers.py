import pytest
from hoerapi.parser import parser_list, parser_object
from hoerapi.errors import InvalidDataError, MissingAttributeError

mockCalled = 0

class MockCounter:
    def __init__(self, data):
        global mockCalled
        mockCalled += 1


class MockSingle:
    def __init__(self, data):
        foo = data['foo']


class TestParserList:
    def setup_method(self, method):
        self.mockCalled = 0

    def test_call_clazz(self):
        global mockCalled; mockCalled = 0
        parser_list(MockCounter, [{}, {}])
        assert mockCalled == 2

    def test_no_array(self):
        with pytest.raises(InvalidDataError):
            parser_list(MockCounter, (None,))

    def test_none(self):
        lst = parser_list(MockCounter, None)
        assert isinstance(lst, list)
        assert len(lst) == 0


class TestParserObject:
    def setup_method(self, method):
        self.mockCalled = 0

    def test_call_clazz(self):
        global mockCalled; mockCalled = 0
        parser_object(MockCounter, [{}, {}])
        assert mockCalled == 1

    def test_missing_attribute(self):
        with pytest.raises(MissingAttributeError):
            parser_object(MockSingle, {})
