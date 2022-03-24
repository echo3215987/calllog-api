# coding:utf-8

import logging
from logging.handlers import TimedRotatingFileHandler

LOG_PATH = "../Log/"

logging.basicConfig()
root = logging.getLogger()
level = logging.INFO
filename = LOG_PATH + ".log"
format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d%(message)s'
#filename, when to changefile, interval, backup count
hdlr = TimedRotatingFileHandler(filename, "midnight", 1, 3)
fmt = logging.Formatter(format)
hdlr.setFormatter(fmt)
root.addHandler(hdlr)
root.setLevel(level)
