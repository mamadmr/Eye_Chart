import json

# read the settings and their options
with open("settings_option.json") as json_string:
    template_json = json.loads(json_string.read())
    print(template_json)

# read the current settings
with open("settings.json") as json_string:
    settings = json.loads(json_string.read())
    print(settings)