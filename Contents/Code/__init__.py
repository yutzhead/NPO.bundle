PLUGIN_TITLE               = 'Nederland 24'
PLUGIN_PREFIX              = '/video/nederland24'

BASE_URL                   = 'http://livestreams.omroep.nl'
CHANNELS = [
  ["101 TV", "101tv.png", "%s/npo/101tv-%s", "Weg met suffe en saaie tv! Het is tijd voor 101 TV, het 24-uurs jongerenkanaal van BNN en de Publieke Omroep. Met rauwe en brutale programma's, van en voor jongeren. Boordevol hilarische fragmenten, spannende livegames, bizarre experimenten en nieuws over festivals en gratis concertkaartjes. Kijken dus!"],
  ["Best 24", "best24.png", "%s/npo/best24-%s", "Best 24 brengt hoogtepunten uit zestig jaar televisiehistorie. Het is een feelgoodkanaal met 24 uur per dag de leukste, grappigste en meest spraakmakende programma's uit de Hilversumse schatkamer. Best 24: de schatkamer van de publieke omroep."],
  ["Consumenten 24", "consumenten24.png", "%s/npo/consumenten24-%s", "Op Consumenten 24 ziet u dagelijks het laatste consumentennieuws en kunt u de hele week kijken naar herhalingen van Radar, Kassa, en vele andere consumentenprogramma's. In Vraag en Beantwoord kunt u live uw vraag stellen per telefoon en webcam."],
  ["Cultura 24", "cultura24.png", "%s/npo/cultura24-%s", "Dit is het 'cultuurkanaal van de Publieke Omroep' met de beste recente en oudere 'kunst en expressie' over verschillende onderwerpen. Klassieke muziek, dans, literatuur, theater, beeldende kunst, film 'Waar cultuur is, is Cultura 24'."],
  ["Familie 24 / Z@ppelin", "familie24.png", "%s/npo/familie24-%s", "Z@ppelin24 zendt dagelijks uit van half drie 's nachts tot half negen 's avonds. Familie24 is er op de tussenliggende tijd. Z@ppelin 24 biedt ruimte aan (oude) bekende peuterprogramma's en je kunt er kijken naar nieuwe kleuterseries. Op Familie24 zijn bekende programma's te zien en nieuwe programma's en documentaires die speciaal voor Familie24 zijn gemaakt of aangekocht."],
  ["Geschiedenis 24", "geschiedenis24.png", "%s/npo/geschiedenis24-%s", "Geschiedenis 24 biedt een actuele, duidende en verdiepende blik op de historie, maar ook een historische blik op de actualiteit. Om de urgentie te vergroten is de programmering thematisch. Ook programma's van Nederland 2 als In Europa, Andere Tijden Sport en De Oorlog zijn gelieerd aan Geschiedenis 24."],
  ["Holland Doc 24", "hollanddoc24.png", "%s/npo/hollanddoc24-%s", "Holland Doc 24 brengt op verschillende manieren en niveaus documentaires en reportages onder de aandacht. De programmering op Holland Doc 24 is gecentreerd rond wekelijkse thema's, die gerelateerd zijn aan de actualiteit, de programmering van documentairerubrieken, van culturele instellingen en festivals."],
  ["Humor TV 24", "humortv24.png", "%s/npo/humortv24-%s", "Humor TV 24 is een uitgesproken comedykanaal: een frisse, Nederlandse humorzender met hoogwaardige, grappige, scherpe, jonge, nieuwe, satirische, humoristische programma's."],
  ["Journaal 24", "journaal24.png", "%s/nos/journaal24-%s", "Via het themakanaal 'Journaal 24' kunnen de live televisieuitzendingen van het NOS Journaal worden gevolgd. De laatste Journaaluitzending wordt herhaald tot de volgende uitzending van het NOS Journaal."],
  ["Politiek 24", "politiek24.png", "%s/nos/politiek24-%s", "Politiek 24 is het digitale kanaal over de Nederlandse politiek in de breedste zin van het woord."],
  ["Spirit 24", "spirit24.png", "%s/npo/spirit24-%s", "Spirit 24 is interreligieus en multicultureel en biedt de kijker een breed aanbod van onderwerpen op het gebied van spiritualiteit, levensbeschouwing, zingeving, cultuur en filosofie, gezien vanuit verschillende geloofsrichtingen en invalshoeken. Spirit 24 laat de kijker genieten en brengt op toegankelijke wijze (nieuwe) inzichten!"],
  ["Sterren 24", "sterren24.png", "%s/npo/sterren24-%s", "Op Sterren 24 zijn de beste Nederlandse artiesten te bewonderen en te beluisteren. Naast clips en uitzendingen uit het rijke TROS-archief is er ruimte voor nieuw materiaal en bieden ze aanstormend Nederlands muziektalent een podium op 24-uurs muziekzender Sterren 24."]
]

SILVERLIGHT_PLAYER         = 'http://www.plexapp.com/player/silverlight.php?stream=%s&width=%d&height=%d&overstretch=fit'

# Default artwork and icon(s)
PLUGIN_ARTWORK             = 'art-default.png'
PLUGIN_ICON_DEFAULT        = 'icon-default.png'

###################################################################################################

def Start():
  Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, PLUGIN_TITLE, PLUGIN_ICON_DEFAULT, PLUGIN_ARTWORK)
  Plugin.AddViewGroup('Details', viewMode='InfoList', mediaType='items')

  # Set the default MediaContainer attributes
  MediaContainer.title1    = PLUGIN_TITLE
  MediaContainer.viewGroup = 'Details'
  MediaContainer.art       = R(PLUGIN_ARTWORK)

###################################################################################################

def MainMenu():
  dir = MediaContainer(noCache=True)

  for channel in CHANNELS:
    url = channel[2] % (BASE_URL, 'bb')
    url = SILVERLIGHT_PLAYER % (url, 534, 300)
    dir.Append(WebVideoItem(url, title=channel[0], thumb=R(channel[1]), summary=channel[3]))

  return dir
