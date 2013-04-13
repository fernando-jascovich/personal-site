#Data Model util
# -*- coding: UTF-8 -*-

try:
    import json
except ImportError:
    import simplejson as json

import os
import sys
import grp
import pwd

relpath = os.path.dirname(__file__)


def createDataModel(self):

    if not os.path.exists(relpath + '/json'):
        os.mkdir(relpath + '/json', 0755)

    with open(relpath + '/json/' + self.name + '.json', 'w') as outfile:
        json.dump(self.pages, outfile)


def getDataModel(self):
    data_model = open(relpath + '/json/' + self + '.json')
    data = json.load(data_model)
    return data
