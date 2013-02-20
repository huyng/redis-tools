#!/usr/bin/env python
"""
Display usage of redis db 

Usage:
    redis-mem-usage.py [--host HOST]

Options:
    --host HOST         # host
   
"""
import redis
from docopt import docopt

def main(host):

    for i in range(15):
        rd = redis.Redis(host=host, db=i)
        keys = rd.keys()
        for k in keys:
            try:
                odbg = rd.debug_object(k)
            except:
                continue
            print "size:%s db:%-10s key:%s" % (odbg.get('serializedlength'), i, k)

    
if __name__ == '__main__':
    opts = docopt(__doc__, version="1.0")
    host = opts['--host']
    main(host)
    
        
    

