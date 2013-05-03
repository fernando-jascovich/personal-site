#Data Model util
# -*- coding: UTF-8 -*-

try:
    import json
except ImportError:
    import simplejson as json

import os
import string
import md5


class BasePage:

    def __init__(self, token):
        self.name = 'base'
        self.pages = {
        "Home": "",
        "Abstract": "",
        "Contact": ""
        }
        self.inputs = {}
        for item in self.pages:
            self.inputs[item] = {"id": sanitize(item), "name": item}

        if token:
            self.token = token
        else:
            uid = md5.new()
            uid.update(os.environ['UNIQUE_ID'])
            self.token = uid.hexdigest()


relpath = os.path.dirname(__file__)


def createDataModel(self):
    if not os.path.exists(relpath + '/json'):
        os.mkdir(relpath + '/json', 0755)

    outfile = open(relpath + '/json/' + self.name + '.json', 'w')

    dumpJson = {}

    for key, value in self.pages.iteritems():
        dumpJson[sanitize(key)] = value

    json.dump(dumpJson, outfile)


def getDataModel(self):
    data_model = open(relpath + '/json/' + self.name + '.json')
    data = json.load(data_model)
    return data


def saveDataModel(model, values):
    if not os.path.exists(relpath + '/json'):
        raise Exception('Data model "' + model.name + '" not found')

    outfile = open(relpath + '/json/' + model.name + '.json', 'w')

    dumpJson = {}

    for item, value in model.pages.iteritems():
        try:
            model.pages[item] = values[item]
            dumpJson[item] = values[item]
        except KeyError:
            dumpJson[item] = model.pages[item]

    json.dump(dumpJson, outfile)


def sanitize(name):
    acceptable_characters = string.ascii_letters + string.digits + '_'
    new_name = ''.join(character for character in name if character in acceptable_characters)
    assert len(new_name) > 0 and new_name[0] not in string.digits + '_', "change %r to %r; is still invalid" % (name, new_name)
    return new_name.lower()
