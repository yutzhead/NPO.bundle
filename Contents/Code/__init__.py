NAME = 'Nederland 24'
SILVERLIGHT_PLAYER = 'http://www.plexapp.com/player/silverlight.php?stream=%s&width=%d&height=%d&overstretch=fit'

CHANNELS = [
	["Nederland 1", "ned1.png", "http://livestreams.omroep.nl/npo/ned1", ""],
	["Nederland 2", "ned2.png", "http://livestreams.omroep.nl/npo/ned2", ""],
	["Nederland 3", "ned3.png", "http://livestreams.omroep.nl/npo/ned3", ""],
	["101 TV", "101tv.png", "http://livestreams.omroep.nl/npo/101tv-bb", "Weg met suffe en saaie tv! Het is tijd voor 101 TV, het 24-uurs jongerenkanaal van BNN en de Publieke Omroep. Met rauwe en brutale programma's, van en voor jongeren. Boordevol hilarische fragmenten, spannende livegames, bizarre experimenten en nieuws over festivals en gratis concertkaartjes. Kijken dus!"],
	["3FM Social Radio Stream", "3fm.png", "http://livestreams.omroep.nl/npo/3fm_vsr-bb", "Kijken via de webcam.\n\nRadio 3FM is altijd de eerste met nieuwe muziek, achtergronden, festivals en de beste DJ's.\n\n3FM is een nationale radiozender van de Nederlandse Publieke Omroep. Het station richt zich vooral op de doelgroep 15 tot en met 35 jaar en zendt grotendeels commerciële rock- en popmuziek uit, met aanvullend elektronische-, house- en dancemuziek."],
	["Best 24", "best24.png", "http://livestreams.omroep.nl/npo/best24-bb", "Best 24 brengt hoogtepunten uit zestig jaar televisiehistorie. Het is een feelgoodkanaal met 24 uur per dag de leukste, grappigste en meest spraakmakende programma's uit de Hilversumse schatkamer. Best 24: de schatkamer van de publieke omroep."],
	["Consumenten 24", "consumenten24.png", "http://livestreams.omroep.nl/npo/consumenten24-bb", "Op Consumenten 24 ziet u dagelijks het laatste consumentennieuws en kunt u de hele week kijken naar herhalingen van Radar, Kassa, en vele andere consumentenprogramma's. In Vraag en Beantwoord kunt u live uw vraag stellen per telefoon en webcam."],
	["Cultura 24", "cultura24.png", "http://livestreams.omroep.nl/npo/cultura24-bb", "Dit is het 'cultuurkanaal van de Publieke Omroep' met de beste recente en oudere 'kunst en expressie' over verschillende onderwerpen. Klassieke muziek, dans, literatuur, theater, beeldende kunst, film 'Waar cultuur is, is Cultura 24'."],
	["Familie 24 / Z@ppelin", "familie24.png", "http://livestreams.omroep.nl/npo/familie24-bb", "Z@ppelin24 zendt dagelijks uit van half drie 's nachts tot half negen 's avonds. Familie24 is er op de tussenliggende tijd. Z@ppelin 24 biedt ruimte aan (oude) bekende peuterprogramma's en je kunt er kijken naar nieuwe kleuterseries. Op Familie24 zijn bekende programma's te zien en nieuwe programma's en documentaires die speciaal voor Familie24 zijn gemaakt of aangekocht."],
	["Geschiedenis 24", "geschiedenis24.png", "http://livestreams.omroep.nl/npo/geschiedenis24-bb", "Geschiedenis 24 biedt een actuele, duidende en verdiepende blik op de historie, maar ook een historische blik op de actualiteit. Om de urgentie te vergroten is de programmering thematisch. Ook programma's van Nederland 2 als In Europa, Andere Tijden Sport en De Oorlog zijn gelieerd aan Geschiedenis 24."],
	["Holland Doc 24", "hollanddoc24.png", "http://livestreams.omroep.nl/npo/hollanddoc24-bb", "Holland Doc 24 brengt op verschillende manieren en niveaus documentaires en reportages onder de aandacht. De programmering op Holland Doc 24 is gecentreerd rond wekelijkse thema's, die gerelateerd zijn aan de actualiteit, de programmering van documentairerubrieken, van culturele instellingen en festivals."],
	["Humor TV 24", "humortv24.png", "http://livestreams.omroep.nl/npo/humortv24-bb", "Humor TV 24 is een uitgesproken comedykanaal: een frisse, Nederlandse humorzender met hoogwaardige, grappige, scherpe, jonge, nieuwe, satirische, humoristische programma's."],
	["Journaal 24", "journaal24.png", "http://livestreams.omroep.nl/nos/journaal24-bb", "Via het themakanaal 'Journaal 24' kunnen de live televisieuitzendingen van het NOS Journaal worden gevolgd. De laatste Journaaluitzending wordt herhaald tot de volgende uitzending van het NOS Journaal."],
	["Politiek 24", "politiek24.png", "http://livestreams.omroep.nl/nos/politiek24-bb", "Politiek 24 is het digitale kanaal over de Nederlandse politiek in de breedste zin van het woord."],
	["Spirit 24", "spirit24.png", "http://livestreams.omroep.nl/npo/spirit24-bb", "Spirit 24 is interreligieus en multicultureel en biedt de kijker een breed aanbod van onderwerpen op het gebied van spiritualiteit, levensbeschouwing, zingeving, cultuur en filosofie, gezien vanuit verschillende geloofsrichtingen en invalshoeken. Spirit 24 laat de kijker genieten en brengt op toegankelijke wijze (nieuwe) inzichten!"],
	["Sterren 24", "sterren24.png", "http://livestreams.omroep.nl/npo/sterren24-bb", "Op Sterren 24 zijn de beste Nederlandse artiesten te bewonderen en te beluisteren. Naast clips en uitzendingen uit het rijke TROS-archief is er ruimte voor nieuw materiaal en bieden ze aanstormend Nederlands muziektalent een podium op 24-uurs muziekzender Sterren 24."]
]

###################################################################################################
def Start():

	ObjectContainer.title1 = NAME

###################################################################################################
@handler('/video/nederland24', NAME)
def MainMenu():

	oc = ObjectContainer()

	for channel in CHANNELS:
		oc.add(CreateVideoClipObject(
			url = SILVERLIGHT_PLAYER % (String.Quote(channel[2]), 640, 360),
			title = channel[0],
			thumb = channel[1],
			summary = channel[3]
		))

	return oc

####################################################################################################
def CreateVideoClipObject(url, title, thumb, summary, include_container=False):

	videoclip_obj = VideoClipObject(
		key = Callback(CreateVideoClipObject, url=url, title=title, thumb=thumb, summary=summary, include_container=True),
		rating_key = url,
		title = title,
		thumb = R(thumb),
		summary = summary,
		items = [
			MediaObject(
				parts = [
					PartObject(key=WebVideoURL(url))
				],
				video_resolution = '360'
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[videoclip_obj])
	else:
		return videoclip_obj
