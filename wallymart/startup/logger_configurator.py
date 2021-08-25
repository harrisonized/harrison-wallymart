#!/usr/bin/env python3

import os
import re
import logging
import datetime as dt


class LoggerConfigurator:
    """Responsible for instantiating the logger used throughout the lifecycle
    of the main program. The logger is configured with a stream_handler, which 
    displays messages to the console, and a file_handler, which outputs the
    messages to a log file.

    :cvar str msg_format: Formats the output string
    :cvar str msg_format: Formats the date. Default is "%Y%m%d %H:%M:%S"
    :ivar Logger logger: Stores an instance of the logger class.
    :ivar str log_dir: The directory of log files.
    :ivar str filename: The base filename of the log file. Note that the actual filename \
    will include the start timestamp of the main program.
    :ivar level: Can use this to toggle between logging.INFO and logging.DEBUG
    """

    msg_format = '%(asctime)s\t' \
                 '%(module)s:%(funcName)s:%(lineno)s\t' \
                 '%(levelname)s\t%(message)s'
    date_format = '%Y%m%d %H:%M:%S'

    def __init__(self,
                 logger=None,
                 log_dir='log',
                 filename='log',
                 level=logging.INFO,
                ):
        if logger is None:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.log_dir = log_dir
        self.filename = filename
        self.level = level
        self.logger.setLevel(self.level)

    # ----------------------------------------------------------------------
    # Private

    def _add_handler(self, handler, msg_format=None):
        if handler=='stream':
            handler = logging.StreamHandler()
        elif handler=='file':
            repo_dir = re.match('^(.*?)harrison-wallymart', os.getcwd()).group()
            log_dir = os.path.dirname(self.log_dir)
            os.makedirs(f'{repo_dir}/{log_dir}', exist_ok=True)
            now = dt.datetime.now().strftime('%Y%m%d_%H%M%S%f')
            handler = logging.FileHandler(f"{self.filename}-{now}.log")
        else:
            raise(KeyError, "Choose one: ['file', 'stream']")
        if msg_format is None:
            msg_format = self.msg_format

        handler.setLevel(self.level)
        formatter = logging.Formatter(msg_format, self.date_format)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    # ----------------------------------------------------------------------
    # Public

    def log(self, msg, level=None):
        if level is None:
            level = self.level
        self.logger.log(level, msg)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def add_stream_handler(self):
        """Enables logger to output to the console.
        """
        self._add_handler('stream', '%(message)s')

    def add_file_handler(self):
        """Enables logger to write to the log file
        """
        self._add_handler('file')
