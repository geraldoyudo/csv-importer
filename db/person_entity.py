import json

class PersonEntity:
    first = ""
    last = ""
    address = ""
    town = ""
    state = ""
    zipcode = ""

    def __init__(self, first, last, address, town='N/A', state='N/A', zipcode='N/A'):
        self.first = first
        self.last = last
        self.address = address
        self.town = town
        self.state = state
        self.zipcode = zipcode