import logging

from logging.handlers import RotatingFileHandler


LOG_FILENAME = 'reader.log'
_log_format = f'%(asctime)s - %(levelname)s - %(name)s - %(message)s'


def get_file_handler():
    file_handler = RotatingFileHandler(LOG_FILENAME,
                                       maxBytes=100000,
                                       backupCount=5,
                                       )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    return logger
