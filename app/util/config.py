import json

COL_BLACK   = (0,       0,      0)
COL_WHITE   = (255,     255,    255)
COL_RED     = (255,     179,    186)
COL_BLUE    = (186,     225,    255)
COL_GREEN   = (186,     255,    201)
COL_ORANGE  = (255,     223,    186)
COL_YELLOW  = (255,     255,    186)

#TODO: not loading every time

def getConfig(key):
    with open('../data/config.json', 'r') as read_file:
        config = json.load(read_file)
        return config[key]