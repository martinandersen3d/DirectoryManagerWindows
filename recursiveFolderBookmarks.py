# recursiveFolderBookmarks.txt
import glob
import os.path 
from pathlib import Path
def recursiveFolderBookmarks():
        fname =  '/media/m/DataLinux/Code/Phyton/RofiDirectoryManager/recursiveFolderBookmarks.txt'
        recursiveList = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        # Check line not empty
                        if line != '\n':
                            path = line.replace('\n', '')
                            directories = glob.glob(path +'/*')
                            for item in directories:
                                if os.path.isdir(item):
                                    name = os.path.basename(item)
                                    recursiveList.append({'name': name, 'path': item})
        return recursiveList
