#!/usr/bin/env python3

import os
import logging
import datetime as dt


class LoggerConfigurator:
    """Wrapper around logger to configure the logger
    """

    msg_format = '%(asctime)s\t' \
                 '%(module)s:%(funcName)s:%(lineno)s\t' \
                 '%(levelname)s\t%(message)s'
    date_format = '%Y%m%d %H:%M:%S'

    def __init__(self, logger=None, filename='log', level=logging.INFO):
        if logger is None:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.filename = filename
        self.level = level

        self.logger.setLevel(self.level)
        self._configure_handler('file')
        self._configure_handler('stream', '%(message)s')

    # ----------------------------------------------------------------------
    # Private

    def _configure_handler(self, handler, msg_format=None):
        if handler=='file':
            now = dt.datetime.now().strftime('%Y%m%d_%H%M%S%f')
            handler = logging.FileHandler(f"{self.filename}-{now}.log")
        elif handler=='stream':
            handler = logging.StreamHandler()
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
