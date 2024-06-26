import os
import sys
import logging


class Logger:
    def __init__(self):
        """
        https://docs.python.org/3/howto/logging.html#loggers
        https://www.loggly.com/ultimate-guide/python-logging-basics/
        https://github.com/IDSIA/sacred/issues/268#issuecomment-459748353

        level       numeric_value
        CRITICAL    50
        ERROR       40
        WARNING     30
        INFO        20
        DEBUG       10
        NOTSET      0
        """

        # get log level
        loglevel = os.getenv("LOG_LEVEL", "INFO")

        # create logger
        self.logger = logging.getLogger("util_logger")
        self.logger.propagate = False
        self.logger.handlers = []
        self.logger.setLevel(loglevel)

        # create console handler and set level to debug
        ch = logging.StreamHandler(sys.stderr)
        ch.setLevel(loglevel)

        # create formatter
        formatter = logging.Formatter("[%(asctime)s] - [%(levelname)s] : %(message)s")

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)

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


# if __name__ == "__main__":
#     log = Logger()

#     log.d("hello debug")
#     log.i("hello info")
#     log.e("hello error")
