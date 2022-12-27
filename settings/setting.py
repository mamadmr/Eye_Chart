import json
import os
import tools

template_json = tools.read_template()

settings = tools.read_settings()

print(template_json)
print(settings)
