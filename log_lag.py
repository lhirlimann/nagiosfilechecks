#!/usr/bin/env python
import os
import sys
import time
from datetime import datetime
from functools import partial

def get_latest_time(fn):
    f = open(fn)
    f.seek(0, os.SEEK_END)
    f.seek(f.tell() - 4096, os.SEEK_SET)
    end = f.read().splitlines()[1:-1] #ignore possibly incomplete first and last lines
    times = [line.split()[0] for line in end]
    timestamps = map(float, times)
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
    if (lag < float(lagvalue)):
        print ("ERROR - File %s lags by %f",fn,lag)
        sys.exit(2)
    else:
        print ("OK - No lag for file %s",fn)
        sys.exit(0)

if __name__ == "__main__":

     lag(sys.argv[1],sys.argv[2])
