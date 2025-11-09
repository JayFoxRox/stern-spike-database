#!/usr/bin/env python3

import sys
import json

state = json.loads(open("./state/state.json", 'rb').read())

indexHtml = "<b>Hello world %d</b>" % (state['value'])

open("./public/index.html", 'wb').write(indexHtml.encode('utf-8'))