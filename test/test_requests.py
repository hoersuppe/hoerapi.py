import pytest
import hoerapi
from datetime import datetime


def test_status():
    status = hoerapi.status()
    assert status is True


def test_get_deleted():
    deleted = hoerapi.get_deleted()
    assert isinstance(deleted, list)

def test_get_deleted_date():
    deleted = hoerapi.get_deleted(dateStart=datetime(2014, 4, 1), dateEnd=datetime(2014, 5, 1))
    assert isinstance(deleted, list)
    assert len(deleted) == 8


def test_get_podcast_data():
    data = hoerapi.get_podcast_data('wrint')
    assert data is not None


def test_get_podcast_data_404():
    with pytest.raises(hoerapi.ApiError):
        hoerapi.get_podcast_data('wr2222int')


def test_get_podcast_episodes():
    episodes = hoerapi.get_podcast_episodes('wrint', 2)
    assert len(episodes) == 2


def test_get_podcast_episodes_404():
    with pytest.raises(hoerapi.ApiError):
        hoerapi.get_podcast_episodes('wr22int')


def test_get_podcast_live():
    live = hoerapi.get_podcast_live('wrint', 3)
    assert len(live) == 3


def test_get_podcast_live_404():
    with pytest.raises(hoerapi.ApiError):
        hoerapi.get_podcast_live('wr222int')


def test_get_live():
    live = hoerapi.get_live(5)
    assert len(live) == 5


def test_get_live_date():
    live = hoerapi.get_live(dateStart=datetime(2014, 12, 8), dateEnd=datetime(2014, 12, 9))
    assert len(live) == 4


def test_get_live_by_id():
    hoerapi.get_live_by_id(3019)


def test_get_live_by_id_404():
    with pytest.raises(hoerapi.ApiError):
        hoerapi.get_live_by_id(0)


def test_get_podcasts():
    pods = hoerapi.get_podcasts()
    assert len(pods) > 0