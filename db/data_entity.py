import json

class DataEntity:
    entityJson = ""

    def __init__(self, data={}):
        self.entityJson = json.dumps(data)