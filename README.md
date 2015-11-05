# hoerapi.py

## Install
```
$ pip install hoerapi
```

## Setup

Use python3.

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install -e .
```

## Tests
```
$ py.test
```

## Usage
```python
import hoerapi;

data = hoerapi.get_podcast_data('wrint')
print(data.cluster) # 'berlin'
```

## Publishing
```
$ python setup.py sdist bdist_dumb upload
```

### Methods
* `status()`
  * returns `True` if the API seems to be up, otherwise `False`
* `get_deleted(dateStart=None, dateEnd=None)`
  * https://github.com/hoersuppe/doc#getdeleted
  * returns: an instance of `DeleteEntry`
* `get_podcast_data(podcast)`
  * https://github.com/hoersuppe/doc#getpodcastdata
  * returns: an instance of `PodcastData`
* `get_podcast_episodes(podcast, count=5)`
  * https://github.com/hoersuppe/doc#getpodcastepisodes
  * returns: an array of `PodcastEpisode`
* `get_podcast_live(podcast, count=5)`
  * https://github.com/hoersuppe/doc#getpodcastlive
  * returns: an array of `PodcastLive`
* `get_live_by_id(id)`
  * https://github.com/hoersuppe/doc#getlivebyid
  * returns: an instance of `PodcastLive`
* `get_live(count=5, dateStart=None, dateEnd=None)`
  * https://github.com/hoersuppe/doc#getlive
  * returns: an array of `PodcastLive`
* `get_podcasts()`
  * https://github.com/hoersuppe/doc#getpodcasts
  * returns: an array of `Podcast`


### Errors
todo


### Classes
* general
  * All date-attributes are converted to `datetime` instances
  * All number-strings are converted to numbers
  * `id` is always lowercase.
* `DeleteEntry`: https://github.com/hoersuppe/doc#getdeleted
* `PodcastData`: https://github.com/hoersuppe/doc#getpodcastdata
  * boolean: `obsolete`, `freeze`, `feature`
  * `contact` is a `PodcastDataContact` instance
* `PodcastDataContact`: contact section of a `PodcastData`
  * all of the attributes may be `None` if there is not data
* `PodcastEpisode`: https://github.com/hoersuppe/doc#getpodcastepisodes
  * `post_`-prefix has been removed
* `PodcastLive`: https://github.com/hoersuppe/doc#getlive
  * boolean: `synced`, `twittered`
* `Podcast`: https://github.com/hoersuppe/doc#getpodcasts
