import colorlog
import logging


def setup_logger(log_file_name=None):
    """
    Setup a logger with colored logs and a file handler.

    Args:
        log_file_name (str, optional): Where do you want to store the logs. Defaults to app.log.

    Returns:
        logger: The configured logger.
    """
    log_file_path = log_file_name if log_file_name else "app.log"

    # Setting up the StreamHandler with colored logs
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s")
    )

    logger = colorlog.getLogger()
    logger.addHandler(handler)

    # Setting up the FileHandler with the log file path
    file_handler = logging.FileHandler(log_file_path)  # Corrected line
    file_handler.setFormatter(
        logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    )  # Removed color formatting for file logs
    logger.addHandler(file_handler)

    return logger
