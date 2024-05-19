import json


def readenvfile():
    with open("C:/Omkarshelkikar/UIAutomation/E2ETesting/testdata/env.json") as envdetails:
        jsondata = json.load(envdetails)
        return jsondata



readenvfile()