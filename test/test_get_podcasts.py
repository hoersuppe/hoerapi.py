import pytest
from hoerapi.get_podcasts import Podcast, PodcastApiResponse


@pytest.mark.parametrize("input,slug,title", [
    ({}, None, None),
    ({ 'slug': 'A', 'title': 'B' }, 'A', 'B'),
])
def test_podcast(input, slug, title):
    podcast = Podcast(input)
    assert podcast.slug == slug
    assert podcast.title == title


@pytest.mark.parametrize("input,podcasts", [
    ([], []),
    ([{}], [Podcast({})]),
    (None, []),
])
def test_podcastApiResponse(input, podcasts):
    resp = PodcastApiResponse(0, 'ok', input)
    assert resp.podcasts == podcasts
