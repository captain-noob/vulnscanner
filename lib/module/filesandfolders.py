import os



def getFullPath(folder):
    return os.path.abspath(folder)


def getAllFiles(path):
    allFiles = []
    for root, _ ,files in os.walk(path):    
        for file in files:
            allFiles.append( os.path.join(root,file))   
    return allFiles


def getAllFolders(path):
    folders = []
    for root, directories, _ in os.walk(path):
        for dir in directories:
            folders.append( os.path.join(root,dir))        
    return folders