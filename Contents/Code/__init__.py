NAME = 'NPO'
BASE_URL = 'http://www.npo.nl/live'

CHANNELS = [
	'npo-1',
	'npo-2',
	'npo-3',
	'npo-nieuws',
	'npo-cultura',
	'npo-101',
	'npo-politiek',
	'npo-best',
	'npo-doc',
	'npo-zappxtra',
	'npo-humor-tv'
]

####################################################################################################
def Start():

	ObjectContainer.title1 = NAME

####################################################################################################
@handler('/video/npo', NAME)
def MainMenu():

	oc = ObjectContainer()

	for channel in CHANNELS:
		url = '%s/%s' % (BASE_URL, channel)
		voc = URLService.MetadataObjectForURL(url)
		voc.url = url
		voc.title = voc.source_title+': '+voc.title
		oc.add(voc)

	return oc
