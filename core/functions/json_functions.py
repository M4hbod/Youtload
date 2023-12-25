import json


class Json:
    @staticmethod
    def get_json(filename):
        with open(filename, "r") as data:
            all_data = json.load(data)

        return all_data

    @staticmethod
    def set_json(filename, key, value):
        with open(filename, "r") as jsonFile:
            data = json.load(jsonFile)

        data[key] = value

        with open(filename, "w") as jsonFile:
            json.dump(data, jsonFile)
