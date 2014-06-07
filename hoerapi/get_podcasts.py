from hoerapi.lowlevel import call_api
from hoerapi.util import CommonEqualityMixin
from hoerapi.parser import parser_list


class Podcast(CommonEqualityMixin):
    def __init__(self, data):
        self.slug = data['slug']
        self.title = data['title']


def get_podcasts():
    return parser_list(Podcast, call_api('getPodcasts'))
