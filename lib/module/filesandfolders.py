import os , codecs
from .loadConfig import getExtensions



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


def getfileExtension(file):
    if os.path.isfile(file):
        return file.split('.')[-1]
    else:
        return None


def filterPHPfiles(path):
    php = getExtensions('php')
    lst=[]
    for ext in php:
        for file in path:
            if getfileExtension(file) == ext:
                lst.append(file)
    return (lst)


def readFile(filename):
    file = codecs.open(filename,encoding="cp437")
    # file =open(filename,encoding="utf-8",errors="replace")
    return file.read()