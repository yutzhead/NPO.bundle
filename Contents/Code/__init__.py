NAME = 'NPO'
BASE_URL_LIVE = 'http://www.npo.nl/live'
BASE_URL_GEMIST = 'http://www.npo.nl/uitzending-gemist'
BASE_URL_GEMIST_DATE = 'http://www.npo.nl/zoeken?utf8=%%E2%%9C%%93&av_type=video&sort_date=%s&page=%s'
BASE_URL_MEESTBEKEKEN = 'http://www.npo.nl/uitzending-gemist/meest-bekeken?date=%s&page=%s'
BASE_URL_AZ = 'http://www.npo.nl/a-z/%s?page=%s'

EPISODE_SUFFIX = '/search?media_type=broadcast&start_date=&end_date=&rows=50'

AZ_RANGE = ['#','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

CHANNELS_LIVE = [
	'npo-1',
	'npo-2',
	'zapp',
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
  Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
  Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

  ObjectContainer.title1 = NAME
  ObjectContainer.view_group = 'List'

####################################################################################################
@handler('/video/npo', NAME)
def MainMenu():
	oc = ObjectContainer()
	for dc in [(Live, 'Live'), (UitzendingGemist, 'Uitzending Gemist'), (MeestBekeken, 'Meest Bekeken'), (AtoZ,'A-Z')]:
		oc.add(DirectoryObject(key=Callback(dc[0]), title=dc[1]))
	return oc

####################################################################################################
def Live():
	oc = ObjectContainer()

	for channel in CHANNELS_LIVE:
		url = '%s/%s' % (BASE_URL_LIVE, channel)
		try: voc = URLService.MetadataObjectForURL(url)
		except: continue
		voc.url = url
		voc.title = voc.source_title+': '+voc.title
		oc.add(voc)

	return oc

####################################################################################################
def AtoZ():
	oc = ObjectContainer()
	for c in AZ_RANGE:
		oc.add(DirectoryObject(key=Callback(AorZ, char=c), title=c.upper()))
	return oc

####################################################################################################
def UitzendingGemist():
	return Select(BASE_URL_GEMIST, 'sort_date', UGDay)

####################################################################################################
def MeestBekeken():
	return Select(BASE_URL_GEMIST, 'most-viewed-date-range', MBDay)

####################################################################################################
def AorZ(char):
	return ListItems(
		BASE_URL_AZ,
		char if char != '#' else '',
		"//div[@class='big-list-item list-item non-responsive row-fluid']",
		'.//h4/text()',
		{'X-Requested-With': 'XMLHttpRequest'},
		char == '#',
		('http://www.npo.nl%s', ListEpisodes)
	)

####################################################################################################
def UGDay(day):
	return ListItems(
		BASE_URL_GEMIST_DATE,
		day,
		'//div[@class="list-item non-responsive row-fluid"]',
		'.//h4/text()'
	)

####################################################################################################
def MBDay(day):
	return ListItems(
		BASE_URL_MEESTBEKEKEN,
		day,
		'//div[@class="list-item tile"]',
		'.//h3/text()'
	)

####################################################################################################
def ListEpisodes(key):
	episodes = ListItems(
		key+EPISODE_SUFFIX,
		'',
		'//div[@class="list-item non-responsive row-fluid"]',
		'.//h4/text()',
		{'X-Requested-With': 'XMLHttpRequest'},
	)
	if len(episodes) == 0:
		episodes = ListItems(
			key+EPISODE_SUFFIX,
			'',
			'//div[@class="list-item tile"]',
			'.//div[@class="contextual-title"]/text()',
			{'X-Requested-With': 'XMLHttpRequest'},
		)
		if len(episodes) == 0:
			episodes = ListItems(
				key+EPISODE_SUFFIX,
				'',
				'//div[@class="row-fluid item"]',
				'.//h3/a/text()',
				{'X-Requested-With': 'XMLHttpRequest'},
			)

	return episodes

####################################################################################################
def Select(url, id, callback):
	oc = ObjectContainer()
	html = HTML.ElementFromURL(url, cacheTime=0)
	options = html.xpath('//select[@id="%s"]' % id)[0].xpath('.//option')

	for o in options:
		title = o.xpath('./text()')[0]
		day = o.xpath('./@value')[0]
		if day == 'no-date':
			continue
		oc.add(DirectoryObject(key=Callback(callback, day=day), title=title))
	return oc

####################################################################################################
def ListItems(url_format, day, xpath, xpath_title, headers={}, charCheck=False, callback=None):
	oc = ObjectContainer()

	page = 0
	while page >= 0:
		page += 1
		if '%s' in url_format:
			html = HTML.ElementFromURL(url_format % (day, page), cacheTime=30, headers=headers)
		else:
			if page > 1: break
			html = HTML.ElementFromURL(url_format, cacheTime=30, headers=headers)

		elements = html.xpath(xpath)
		if len(elements) == 0:
			break

		for i in elements:
			title = i.xpath(xpath_title)[0].strip()
			if charCheck and not title[0].isdigit():
				page = -1
				break

			try:
				summary = i.xpath('.//p/text()')[0]
			except:
				try:
					summary = i.xpath('.//p/span/text()')[0]
					try:
						summary += i.xpath('.//p/span/text()')[2]
					except:
						try:
							summary = i.xpath('.//h5/text()')[0]
						except:
							raise
				except:
					summary = ''

			thumb = i.xpath('.//img/@src')[0]
			url = i.xpath('.//a/@href')[0]

			if callback:
				oc.add(DirectoryObject(
					title = title,
					summary = summary,
					thumb = Resource.ContentsOfURLWithFallback(thumb),
					key = Callback(callback[1], key=callback[0] % url)
				))

			else:
				oc.add(VideoClipObject(
					title = title,
					summary = summary,
					thumb = Resource.ContentsOfURLWithFallback(thumb),
					url = 'http://npo.nl'+url
				))

	return oc
