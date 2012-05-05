import logging
import os 
import sys
import time

loglevel = sys.argv[1]

loglevel_number = getattr(logging, loglevel.upper(),None)

if not isinstance(loglevel_number, int):
	print '''
Invalid Log Level - "%s"
Log Level must be one of the following:
1. INFO
2. WARNING
3. DEBUG 

''' % loglevel

logging.basicConfig(level=loglevel_number)
