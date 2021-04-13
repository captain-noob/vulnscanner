from .module.filesandfolders import getAllFiles ,getFullPath ,filterPHPfiles ,readFile
from .module.fileAnalyzer import FileAnalyzer
from .module.injections import Injection
import os




def scanner(file):
    content = readFile(file)
    analyze = FileAnalyzer(file,content)
    phpstringlist = analyze.readPHPString()
    injection = Injection(file,phpstringlist)
    # injection.sqlInjection()
    injection.commandInjection()



def runner(path):
    fullpath=getFullPath(path)
    if os.path.isdir(fullpath):
        files = getAllFiles(fullpath)
        files = filterPHPfiles(files)
        for file in files:
            scanner(file)
    
    else:
        print('This is not a directory.')
            

def fileRunner(path):
    fullpath=getFullPath(path)
    if os.path.isfile(fullpath):
        scanner(fullpath)
    else:
        print('This is not a file.')
    




def main(path):
    # path='../../web/eduapp_web_api'
    # path='C:\\xampp\\htdocs\\crime'
    # path='C:\\xampp\\htdocs\\e-seva'
    # path='../DVWA'
    # path='../Vulnerable-Web-Application'
    # path='../Art-gallery'
    fullpath=getFullPath(path)
    runner(fullpath)