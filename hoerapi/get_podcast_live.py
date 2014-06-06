from hoerapi.lowlevel import ApiResponse, call_api, parse_date
from hoerapi.CommonEqualityMixin import CommonEqualityMixin


class PodcastLive(CommonEqualityMixin):
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.podcast = data.get('podcast', '')
        self.state = int(data.get('state', 0))
        self.type = int(data.get('type', 0))
        self.synced = int(data.get('synced', 0))
        self.title = data.get('title', '')
        self.url = data.get('url', '')
        self.streamurl = data.get('streamurl', '')
        self.livedate = parse_date(data.get('livedate', None))
        self.duration = int(data.get('duration', 0))
        self.twittered = data.get('twittered', '')


class PodcastLiveApiResponse(ApiResponse):
    def __init__(self, status, msg, events):
        ApiResponse.__init__(self, status, msg)

        self.events = []

        if events is not None:
            for pod in events:
                self.events.append(PodcastLive(pod))


def get_podcast_live(podcast, count=5):
    return call_api('getPodcastLive', PodcastLiveApiResponse, {
        'podcast': podcast,
        'count': count,
    })
