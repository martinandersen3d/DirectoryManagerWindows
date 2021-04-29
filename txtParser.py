# Bookmark_folders.txt
import os.path 
from pathlib import Path
def txtBookmarksTxtFile():
        fname =  '/media/m/DataLinux/Code/Phyton/RofiDirectoryManager/bookmark_folders.txt'
        bookmarkList = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        # Check line not empty
                        if line != '\n':
                                path = line.replace('\n', '')
                                name = os.path.basename(path)
                                bookmarkList.append({'name': name, 'path': path})
        return bookmarkList
        # print(content_array)


