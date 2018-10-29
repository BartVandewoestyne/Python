import logging.config

mylogger = logging.config.dictConfig('logging.conf')
mylogger.debug("test")
