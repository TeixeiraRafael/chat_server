import sys

from ChatRoom import *

cr = ChatRoom('127.0.0.1', int(sys.argv[1]))
cr.start()