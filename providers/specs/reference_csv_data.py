import json

referenceCSVData = [
    {
        "first": "John",
        "last": "Doe",
        "address": "120 jefferson st.",
        "town": "Riverside",
        "state": "NJ",
        "pobox": "08075",
    },
    {
        "first": "Jack",
        "last": "McGinnis",
        "address": "220 hobo Av.",
        "town": "Phila",
        "state": "PA",
        "pobox": "09119"
    }
]

referenceJSONData = []
for data in referenceCSVData:
    referenceJSONData.append(json.dumps(data))