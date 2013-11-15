import urllib.request
import xml.dom.minidom as dom
import re
   
class RSSFeed:
   
	def __init__(self, url, parent=None):
		super(RSSFeed, self).__init__()
  
		self.resp = urllib.request.urlopen(url)
		self.data = self.resp.read()
		self.dataEncoded = self.data.decode('UTF-8')
		self.xmlFile = dom.parseString(self.dataEncoded)
  
	def searchTag(self, seriesName, tag):
		self.tag = tag
  
		for node in self.xmlFile.getElementsByTagName(self.tag):
 			description = node.getElementsByTagName('title')
 			if seriesName.lower() in description[0].toxml().lower():
 				print(seriesName)
 				print(self.getEpisode(description[0].toxml()))
                           
	def getEpisode(self, title):
		self.title = title
		matches = re.search("S(\d+)E(\d+)", self.title, re.I).groups()
		return matches    
