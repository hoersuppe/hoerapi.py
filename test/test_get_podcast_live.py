import pytest
from hoerapi.get_podcast_live import PodcastLive
from datetime import datetime


def test_podcastLive_livedate():
    live = PodcastLive({
        'livedate': '2012-12-02 13:00:00'
    })
    assert live.livedate == datetime(2012, 12, 2, 13, 0, 0)
