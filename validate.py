import json

for file_name in ("geofeed_large.csv", "geofeed.csv"):
    with open(file_name) as file:
        for index, row in enumerate(file):
            num_fields = len(row.split(","))
            if num_fields != 5:
                print(index, json.dumps(row), num_fields)
