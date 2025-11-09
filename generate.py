#!/usr/bin/env python3

import sys
import json

statePath = sys.argv[1]
pagesPath = sys.argv[2]

state = json.loads(open(statePath + "/state.json", 'rb').read())

indexHtml = "<b>Hello world %d</b>" % (state['value'])

open(pagesPath + "/index.html", 'wb').write(indexHtml.encode('utf-8'))


