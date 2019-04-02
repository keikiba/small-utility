import logging
from logging import Formatter, FileHandler, StreamHandler, getLogger
import datetime as dt

class Logger:
    # Log format
    handler_format = Formatter(
        fmt='%(asctime)s %(name)s [%(levelname)5s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    def __init__(self, opts):

        self.logfile = ''
        self.console = False
        self.loglevel = logging.DEBUG
        self.program_name = opts['program_name']
        self.logger = getLogger(self.program_name)
        self.logger.setLevel(logging.DEBUG)

        # Log level
        if 'LogLevel' in opts and opts['LogLevel'] != '':
            lvl = opts['LogLevel'].lower()
            if lvl == 'debug':
                self.loglevel = logging.DEBUG
            elif lvl == 'info':
                self.loglevel = logging.INFO
            elif lvl == 'warn':
                self.loglevel = logging.WARN
            elif lvl == 'error':
                self.loglevel = logging.ERROR
            elif lvl == 'critical':
                self.loglevel = logging.CRITICAL
            else:
                pass

        # STDOUT
        if 'LogConsole' in opts and opts['LogConsole'] == 'True':
            self.console = True
            stream_handler = StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            stream_handler.setFormatter(Logger.handler_format)
            self.logger.addHandler(stream_handler)

        # File handler        
        if 'LogFile' in opts and opts['LogFile'] != '':
            self.logfile = opts['LogFile']
            file_handler = FileHandler(self.logfile, 'w')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(Logger.handler_format)
            self.logger.addHandler(file_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


def test_main():
    opts = {
        'program_name': 'TEST',
        'LogFile': '',
        'LogConsole': 'True',
        'LogLevel': 'debug'
    }
    mylog = Logger(opts)
    mylog.debug("debug message")
    mylog.info("info message")
    mylog.warn("warn message")
    mylog.error("error message")
    mylog.critical("critical message")
    test_submodule()
    mylog.debug("debug message from main()")

def test_submodule():
    mysublog = getLogger('TEST').getChild('SUB')
    mysublog.debug("debug message from submodule()")

if __name__ == "__main__":
    test_main()
