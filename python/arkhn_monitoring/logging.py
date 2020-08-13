from fluent import handler
import logging


class CustomFilter(logging.Filter):
    def __init__(self, extra_fields):
        self.extra_fields = extra_fields

    def filter(self, record):
        for field in self.extra_fields:
            if not hasattr(record, field):
                setattr(record, field, None)
        return True


def create_logger(service_name, fluentd_host, fluentd_port, level=None, extra_fields=[]):
    """
    Create a logger with a FluentHandler.
    Args:
        service_name (str): name of the service from which the logging is done
        fluentd_host (str): host of fluentd service
        fluentd_port (int): port of fluentd service
        level (str): the logging level ("INFO", "DEBUG", ...)
        extra_fields (list of str): a list of extra fields to log
    Returns:
        Logger: the object to use to log messages
    """
    custom_format = {
        "where": "%(module)s.%(funcName)s",
        "type": "%(levelname)s",
        "service": service_name,
    }

    if not isinstance(extra_fields, list):
        raise ValueError("create_fluent_logger: extra_fields should be a list.")

    for field in extra_fields:
        custom_format[field] = f"%({field})s"

    logger = logging.getLogger(service_name)
    logger.propagate = False

    h = handler.FluentHandler(service_name, host=fluentd_host, port=fluentd_port)
    formatter = handler.FluentRecordFormatter(custom_format)
    h.setFormatter(formatter)
    logger.addHandler(h)
    logger.addFilter(CustomFilter(extra_fields))
    logger.setLevel(level or getattr(logging, level))

    return logger
