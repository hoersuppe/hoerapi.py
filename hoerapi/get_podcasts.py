from hoerapi.lowlevel import ApiResponse, call_api
from hoerapi.CommonEqualityMixin import CommonEqualityMixin


class Podcast(CommonEqualityMixin):
    def __init__(self, data):
        self.slug = data.get('slug', None)
        self.title = data.get('title', None)


class PodcastsApiResponse(ApiResponse):
    def __init__(self, status, msg, podcasts):
        ApiResponse.__init__(self, status, msg)

        self.podcasts = []

        if podcasts is not None:
            for pod in podcasts:
                self.podcasts.append(Podcast(pod))


def get_podcasts():
    return call_api('getPodcasts', PodcastsApiResponse, {})
