#!/usr/bin/env python3
from RssReader import rssReader
from os import system
import subprocess

class notifyFormat:

    def __init__(self, url, tag):
        self.rssReader = rssReader(url)
        self.uElementList = self.rssReader.createList(tag)
        self.elementList = self.rssReader.readList('updatedList')
        self.newEntryList = self.rssReader.compare(self.uElementList, self.elementList)
        
        self.rssReader.saveList('updatedList', self.uElementList)
        self.notify()

    def notify(self):
        for element in self.newEntryList:
            self.line = self.clearTags(element)
            subprocess.Popen(['notify-send', "Anime: " + self.line])

    def clearTags(self, line):
        self.line = line
        self.line = self.line[:-8]
        self.line = self.line.strip('<title>')
        return self.line


