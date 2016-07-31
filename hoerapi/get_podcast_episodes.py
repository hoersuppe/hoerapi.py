from hoerapi.lowlevel import call_api
from hoerapi.parser import parser_list
from hoerapi.util import CommonEqualityMixin, parse_date


class PodcastEpisode(CommonEqualityMixin):
    def __init__(self, data):
        self.id = int(data['ID'])
        self.date = parse_date(data['post_date'])
        gmt = data.get('post_date_gmt')
        self.date_gmt = parse_date(gmt, 'gmt') if gmt else None
        self.name = data['post_name']
        self.modified = parse_date(data['post_modified'])
        gmt = data.get('post_date_gmt')
        self.modified_gmt = parse_date(gmt, 'gmt') if gmt else None
        self.link = data['post_link']
        self.commentlink = data['post_commentlink']
        self.mediaurl = data['post_mediaurl']
        self.duration = int(data['post_duration'])


def get_podcast_episodes(podcast, count=5):
    return parser_list(PodcastEpisode, call_api('getPodcastEpisodes', {
        'podcast': podcast,
        'count': count,
    }))
