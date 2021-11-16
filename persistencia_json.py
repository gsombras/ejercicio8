#Store data
import json

def store(var, filename):
    json.dump(json.dumps(list), open("Coches.txt", "w"))

def retrive(filename):
    return json.loads(json.load(open(filename, 'r')))
