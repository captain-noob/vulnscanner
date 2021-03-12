import os,sys
import json
CONFIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'../config'))


def getExtensions(type):
    path = os.path.join(CONFIG_DIR,'extenstion.json')
    data = open(path).read()
    data = json.loads(data)
    for i in data:
        if i['type'] == type:
            return(i['extensions'])