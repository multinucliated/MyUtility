
from datetime import datetime
import logging
import os

DATE_FORMAT = '%d-%m-%Y'
SUCESS_FILENAME = 'success_logs/ProjectName-{}.log'
ERROR_FILENAME = 'error_logs/ProjectName-{}.log'
DIRECTORY_SUCCESS = "success_logs/"
DIRECTORY_ERROR = "error_logs/"
FORMAT_LOGGING = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s:%(message)s'
DATA_ADDED_LOG = 'data is added to database '
DATA_ERROR_LOG = 'data is not to database '
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def set_success_logger():
    """
    This will create the sucess logs.
    :return: Null
    """


    today = datetime.today().strftime(DATE_FORMAT)
    filename = SUCESS_FILENAME.format(today)

    if not os.path.exists(DIRECTORY_SUCCESS):
        os.makedirs(DIRECTORY_SUCCESS)

    logging.basicConfig(
        filename=filename, level=logging.DEBUG,
        format=FORMAT_LOGGING,
        datefmt=DATE_TIME_FORMAT
    )

    logging.debug(DATA_ADDED_LOG)


def set_error_logger():
    """
    This will create the error logs.
    :return: Null
    """


    today = datetime.today().strftime(DATE_FORMAT)
    filename = ERROR_FILENAME.format(today)

    if not os.path.exists(DIRECTORY_ERROR):
        os.makedirs(DIRECTORY_ERROR)

    logging.basicConfig(
        filename=filename, level=logging.DEBUG,
        format=FORMAT_LOGGING,
        datefmt=DATE_TIME_FORMAT
    )
    logging.debug(DATA_ERROR_LOG)
