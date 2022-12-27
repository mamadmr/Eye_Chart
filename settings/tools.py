import json
import os


def read_template():
    with open("settings_option.json") as json_string:
        template_json = json.loads(json_string.read())
    return template_json


def write_settigs(settings):
    with open("settings.json", 'w') as json_file:
        json.dump(settings, json_file)


def read_settings():
    if os.stat("settings.json").st_size == 0:
        settings = {"cursor": 0}
        for option in read_template().items():
            settings[option[0]] = 0
        write_settigs(settings)

    with open("settings.json") as json_string:
        settings = json.loads(json_string.read())
    
    return settings