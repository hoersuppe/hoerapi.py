from lowlevel import ApiResponse, call_api


class Podcast:
    def __init__(self, slug, title):
        self.slug = slug
        self.title = title

    slug = ''
    title = ''


class PodcastApiResponse(ApiResponse):
    def __init__(self, status, msg, podcasts):
        ApiResponse.__init__(self, status, msg)

        self.podcasts = []

        for pod in podcasts:
            self.podcasts.append(Podcast(pod['slug'], pod['title']))


def get_podcasts():
    return call_api('getPodcasts', PodcastApiResponse, {})
