#!/usr/bin/env python3
import urllib.request
import xml.dom.minidom as dom

class rssReader:
    
    def __init__(self, url):
        self.url = url

        resp = urllib.request.urlopen(self.url)
        data = resp.read()
        text = data.decode('UTF-8')
        self.xmlDocument = dom.parseString(text)

    def searchTag(self, tag):
        self.tag = tag

        for node in self.xmlDocument.getElementsByTagName(self.tag):
            print(node.toxml())

    def createList(self, tag):
        self.tag = tag
        self.elementList = []

        for node in self.xmlDocument.getElementsByTagName(self.tag):
            self.elementList.append(node.toxml())
        return self.elementList

    def compare(self, updatedList, oldList):
        self.updatedList = updatedList
        self.oldList = oldList
        self.newUpdateList = []

        for uElement in self.updatedList:
            if not uElement in self.oldList:
                self.newUpdateList.append(uElement)
        return self.newUpdateList

    def saveList(self, fileName, saveList):
        self.saveList = saveList

        outFile = open(fileName, "wt")
        for element in self.saveList:
            outFile.write(element + " \n")
        outFile.close()

    def readList(self, fileName):
        self.list = []
        self.aList = []
        self.fileName = fileName

        inFile = open(self.fileName, "rt")
        while True:
            line = inFile.readline()
            if(len(line) == 0):
                break
            else:
                self.list.append(line)
        inFile.close()
        for element in self.list:
            self.aList.append(element.strip())
        return self.aList
