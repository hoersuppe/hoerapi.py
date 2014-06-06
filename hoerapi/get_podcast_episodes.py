from hoerapi.lowlevel import ApiResponse, call_api, parse_date
from hoerapi.CommonEqualityMixin import CommonEqualityMixin


class PodcastEpisode(CommonEqualityMixin):
    def __init__(self, data):
        self.id = int(data.get('post_id', 0))
        self.date = parse_date(data.get('post_date', None))
        self.date_gmt = parse_date(data.get('post_date_gmt', None))
        self.name = data.get('post_name', '')
        self.modified = parse_date(data.get('post_modified', None))
        self.modified_gmt = parse_date(data.get('post_modified_gmt', None))
        self.link = data.get('post_link', '')
        self.commentlink = data.get('post_commentlink', '')
        self.mediaurl = data.get('post_mediaurl', '')
        self.duration = int(data.get('post_duration', 0))


class PodcastEpisodesLiveApiResponse(ApiResponse):
    def __init__(self, status, msg, episodes):
        ApiResponse.__init__(self, status, msg)

        self.episodes = []

        if episodes is not None:
            for episode in episodes:
                self.events.append(PodcastEpisode(episode))


def get_podcast_episodes(podcast, count=5):
    return call_api('getPodcastEpisodes', PodcastEpisodesLiveApiResponse, {
        'podcast': podcast,
        'count': count,
    })
