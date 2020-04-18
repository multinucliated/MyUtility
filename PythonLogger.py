import logging
import os
from datetime import datetime

DATE_FORMAT = '%d-%m-%Y'
SUCESS_FILENAME = 'success_logs/ProjectName-{}.log'
ERROR_FILENAME = 'error_logs/ProjectName-{}.log'
DIRECTORY_SUCCESS = "success_logs/"
DIRECTORY_ERROR = "error_logs/"
FORMAT_LOGGING = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s:%(message)s'

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def log_this_logger(exe):
    """
    This will log the message from the exe variable
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

    logging.debug(exe)
