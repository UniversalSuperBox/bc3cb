import os
from os import path
import logging
from logging.config import fileConfig
logging.config.fileConfig('bc3cb.ini', disable_existing_loggers=False)
logger = logging.getLogger('bc3cbCore')
