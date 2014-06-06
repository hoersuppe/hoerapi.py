from hoerapi.lowlevel import ApiResponse, call_api


class Podcast:
    def __init__(self, data):
        self.slug = data.get('slug', '')
        self.title = data.get('title', '')


class PodcastApiResponse(ApiResponse):
    def __init__(self, status, msg, podcasts):
        ApiResponse.__init__(self, status, msg)

        self.podcasts = []

        for pod in podcasts:
            self.podcasts.append(Podcast(pod))


def get_podcasts():
    return call_api('getPodcasts', PodcastApiResponse, {})
