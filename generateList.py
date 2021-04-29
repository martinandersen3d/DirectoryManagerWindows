import os
import subprocess

from txtParser import txtBookmarksTxtFile
from recursiveFolderBookmarks import recursiveFolderBookmarks


def generateList():
    # recentList = iniRecentDocumentsFolders()
    # workspaceList = jsonVsCodeWorkspaces()
    # deviceList = jsonDevices()
    # placeList = xmlDolpginPlaces()
    bookmarkList = txtBookmarksTxtFile()
    recursiveList = recursiveFolderBookmarks()

    # merge Lists into one List
    # fullList = recentList + workspaceList + deviceList + bookmarkList + placeList + recursiveList
    fullList = bookmarkList + recursiveList

    # Fix:  sometimes path will show as "%20" when there is a space,
    #       this will convert it to normal spaces.
    for item in fullList:
        item['name'] = item['name'].replace('%20', ' ')
        item['path'] = item['path'].replace('%20', ' ')
    

    # res = list(map(dict, set(tuple(sorted(sub.items())) for sub in fullList))) 
    filtered = {v['name']:v for v in fullList}.values()
    sortedList = sorted(filtered, key=lambda k: (k['name']).lower()) 
    resultList=[]
    for item in sortedList:
        resultList.append(item['path'])

    return tuple(sorted(list(set(resultList))))

