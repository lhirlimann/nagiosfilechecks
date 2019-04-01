#!/usr/bin/env python
import os
import sys
import time
from datetime import datetime
from functools import partial
DEFAULT_LOG = "/usr/local/bro/logs/current/conn.log"

def get_latest_time(fn):
    f = open(fn)
    timestamps = []
    f.seek(-4096, os.SEEK_END)
    end = f.read().splitlines()[1:-1] #ignore possibly incomplete first and last lines
    times = [line.split()[0] for line in end]
    for items in times:
        k = time.strptime(items,"%Y-%m-%dT%H:%M:%SZ")
        timestamps.append(time.mktime(k))

    latest = max(timestamps)
    return latest

def lag(fn, lagvalue):
    try :
        latest = get_latest_time(fn)
    except (IOError, ValueError):
        #File could be rotating, wait and try again
        time.sleep(10)
        latest = get_latest_time(fn)
    now = time.time()
    lag = now - latest
    if (lag < lagvalue):
        print "ERROR - File % lags by %f",fn,lag
        sys.exit(2)
    else:
        print "OK - No lag for file %s",fn
        sys.exit(0)

if __name__ == "__main__":

#    filename = os.getenv("BRO_LAG_FILENAME", DEFAULT_LOG)

#    if sys.argv[1:] and sys.argv[1] == 'config':
#        config()
#    else:
#        lag(filename,lag)
     print("file %s , lag %f",sys.argv[1],sys.argv[2])
     lag(sys.argv[1],sys.argv[2])
