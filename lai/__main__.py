import sys
from .application import Application

application = Application()
application.apply(sys.argv[1:])