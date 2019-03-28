#!/usr/bin/env python
import os
import sys
import time

DEFAULT_LOG = "/usr/local/bro/logs/current/conn.log"

def config():
    print """
graph_category network

graph_title Bro log lag
graph_vlabel lag
graph_args --base 1000 --vertical-label seconds --lower-limit 0
graph_info The bro log lag

lag.label lag
lag.info log message lag in seconds
lag.min 0
lag.warning :5000
lag.warning 0:15
lag.critical 0:60
""".strip()

    return 0

def get_latest_time(fn):
    f = open(fn)

    f.seek(-4096, os.SEEK_END)
    end = f.read().splitlines()[1:-1] #ignore possibly incomplete first and last lines
    times = [line.split()[0] for line in end]
    timestamps = map(float, times)
    latest = max(timestamps)
    return latest

def lag(fn):
    try :
        latest = get_latest_time(fn)
    except (IOError, ValueError):
        #File could be rotating, wait and try again
        time.sleep(10)
        latest = get_latest_time(fn)
    now = time.time()
    lag = now - latest
    print "lag.value %f" % lag

if __name__ == "__main__":

    filename = os.getenv("BRO_LAG_FILENAME", DEFAULT_LOG)

    if sys.argv[1:] and sys.argv[1] == 'config':
        config()
    else:
        lag(filename)
