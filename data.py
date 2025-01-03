import json

data = {}

def init():
    global data
    with open('config.json', 'r') as f:
        data = json.loads(f.read())

def get_value(key: str):
    return data[key]
