from hoerapi.lowlevel import ApiResponse, call_api


class PodcastDataContact:
    def __init__(self, data):
        self.twitter = data.get('twitter', '')
        self.adn     = data.get('adn', '')
        self.email   = data.get('email', '')


class PodcastData:
    def __init__(self, data):
        self.ID = data.get('ID', 0)
        self.title = data.get('title', '')
        self.description = data.get('description', '')
        self.url = data.get('url', '')
        self.feedurl = data.get('feedurl', '')
        self.imageurl = data.get('imageurl', '')
        self.slug = data.get('slug', '')
        self.recension = data.get('recension', '')
        self.cluster = data.get('cluster', '')
        self.rec_pos = data.get('rec_pos', '')
        self.rec_neg = data.get('rec_neg', '')
        self.chat_server = data.get('chat_server', '')
        self.chat_channel = data.get('chat_channel', '')
        self.chat_url = data.get('chat_url', '')
        self.obsolete = data.get('obsolete', '')
        self.freeze = data.get('freeze', '')
        self.stream = data.get('stream', '')
        self.otitle = data.get('otitle', '')
        self.feature = data.get('feature', '')
        self.contact = PodcastDataContact(data.get('contact', {}))


class PodcastDataApiResponse(ApiResponse):
    def __init__(self, status, msg, data):
        ApiResponse.__init__(self, status, msg)

        self.data = PodcastData(data)


def get_podcast_data(podcast):
    return call_api('getPodcastData', PodcastDataApiResponse, { 'podcast': podcast })
