import json

reference_csv_data = [
    {
        "first": "John",
        "last": "Doe",
        "address": "120 jefferson st.",
        "town": "Riverside",
        "state": "NJ",
        "zipcode": "08075",
    },
    {
        "first": "Jack",
        "last": "McGinnis",
        "address": "220 hobo Av.",
        "town": "Phila",
        "state": "PA",
        "zipcode": "09119"
    }
]

reference_json_data = []
for data in reference_csv_data:
    reference_json_data.append(json.dumps(data))
