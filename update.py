#!/usr/bin/env python3

import sys
import json

state = json.loads(open("./state/state.json", 'rb').read())

state['value'] += 1

open("./state/state.json", 'wb').write(json.dumps(state).encode('utf-8'))