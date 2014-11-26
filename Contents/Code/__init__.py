NAME = 'Nederland 24'
BASE_URL = 'http://www.npo.nl/live'

CHANNELS = [
	{
		'name': 'NPO 1',
		'icon': 'https://dl.dropboxusercontent.com/u/2974527/Plex/Nederland-24/ned1.png',
		'slug': 'npo-1'
	},
	{
		'name': 'NPO 2',
		'icon': 'https://dl.dropboxusercontent.com/u/2974527/Plex/Nederland-24/ned2.png',
		'slug': 'npo-2'
	},
	{
		'name': 'NPO 3',
		'icon': 'https://dl.dropboxusercontent.com/u/2974527/Plex/Nederland-24/ned3.png',
		'slug': 'npo-3'
	},
	{
		'name': 'NPO Nieuws',
		'icon': '',
		'slug': 'npo-nieuws'
	},
	{
		'name': 'NPO Cultura',
		'icon': '',
		'slug': 'npo-cultura'
	},
	{
		'name': 'NPO 101',
		'icon': '',
		'slug': 'npo-101'
	},
	{
		'name': 'NPO Politiek',
		'icon': '',
		'slug': 'npo-politiek'
	},
	{
		'name': 'NPO Best',
		'icon': '',
		'slug': 'npo-best'
	},
	{
		'name': 'NPO Doc',
		'icon': '',
		'slug': 'npo-doc'
	},
	{
		'name': 'NPO Zapp Xtra',
		'icon': '',
		'slug': 'npo-zappxtra'
	},
	{
		'name': 'NPO Humor TV',
		'icon': '',
		'slug': 'npo-humor-tv'
	}
]

####################################################################################################
def Start():

	ObjectContainer.title1 = NAME

####################################################################################################
@handler('/video/nederland24', NAME)
def MainMenu():

	oc = ObjectContainer()

	for channel in CHANNELS:
		oc.add(VideoClipObject(
			url = '%s/%s' % (BASE_URL, channel['slug']),
			title = channel['name'],
			thumb = Resource.ContentsOfURLWithFallback(channel['icon'])
		))

	return oc
