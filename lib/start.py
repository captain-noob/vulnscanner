from .module.filesandfolders import getAllFiles ,getFullPath
import os


def runner(fullpath):
    if os.path.isdir(fullpath):
        files = getAllFiles(fullpath)
        # files = getPHPFiles(files)
        # for file in files:
        #     check(file)




def main():
    # path='../../web/eduapp_web_api'
    # path='C:\\xampp\\htdocs\\crime'
    # path='C:\\xampp\\htdocs\\e-seva'
    # path='../DVWA'
    # path='../Vulnerable-Web-Application'
    path='../Art-gallery'
    fullpath=getFullPath(path)
    runner(fullpath)