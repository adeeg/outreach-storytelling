import json

#TODO: not loading every time

def getConfig(key):
    with open('../data/config.json', 'r') as read_file:
        config = json.load(read_file)
        return config[key]