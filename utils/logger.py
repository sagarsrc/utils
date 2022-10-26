"""
logger class
"""

import os
import logging


class Logger:
    def __init__(self):
        """
        https://docs.python.org/3/howto/logging.html#loggers
        https://www.loggly.com/ultimate-guide/python-logging-basics/

        level       numeric_value
        CRITICAL    50
        ERROR       40
        WARNING     30
        INFO        20
        DEBUG       10
        NOTSET      0
        """

        # get log level
        loglevel = os.environ.get("LOG_LEVEL", "INFO")

        # create logger
        logger = logging.getLogger("util_logger")
        logger.setLevel(loglevel)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        # create formatter
        formatter = logging.Formatter("[%(asctime)s] - [%(levelname)s] : %(message)s")

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        self.logger = logger

        # print(loglevel, self.logger)

    def d(self, msg):
        self.logger.debug(msg)

    def i(self, msg):
        self.logger.info(msg)

    def w(self, msg):
        self.logger.warning(msg)

    def e(self, msg):
        self.logger.error(msg)

    def c(self, msg):
        self.logger.critical(msg)


if __name__ == "__main__":
    log = Logger()

    log.d("hello debug")
    log.i("hello info")
    log.e("hello error")
