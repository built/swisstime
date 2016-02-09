__version__ = '0.9.0'

import time

TICK = None
TOCK = None
MOMENTS = []

def start():
    global TICK
    global TOCK
    global MOMENTS
    MOMENTS = []
    TOCK = None
    TICK = time.clock()

def tick(label=""):
    global TICK
    global TOCK
    global MOMENTS
    TOCK = time.clock()
    MOMENTS.append((label, (TOCK - TICK)))
    TICK = TOCK

def report():
    global MOMENTS
    output = ("-" * 50) + "\n"
    output += "Time in seconds\n"
    output += ("-" * 50) + "\n"
    for entry in MOMENTS:
        output += "%f | %s\n" % (entry[1], entry[0])
    return output

def data():
    global MOMENTS
    return MOMENTS



