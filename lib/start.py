from .module.filesandfolders import getAllFiles ,getFullPath ,filterPHPfiles ,readFile
from .module.fileAnalyzer import FileAnalyzer
from .module.injections import Injection
import os


def runner(fullpath):
    if os.path.isdir(fullpath):
        files = getAllFiles(fullpath)
        files = filterPHPfiles(files)
        for file in files:
            content = readFile(file)
            analyze = FileAnalyzer(file,content)
            phpstringlist = analyze.readPHPString()
            injection = Injection(file,phpstringlist)
            injection.sqlInjection()
            injection.commandInjection()
            




def main():
    # path='../../web/eduapp_web_api'
    # path='C:\\xampp\\htdocs\\crime'
    # path='C:\\xampp\\htdocs\\e-seva'
    path='../DVWA'
    # path='../Vulnerable-Web-Application'
    # path='../Art-gallery'
    fullpath=getFullPath(path)
    runner(fullpath)