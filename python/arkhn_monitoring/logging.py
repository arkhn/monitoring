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


def create_fluent_logger(service_name, fluentd_host, fluentd_port, level=None, extra_fields=[]):
    """
    Create a logger with a FluentHandler.
    """
    custom_format = {
        "where": "%(module)s.%(funcName)s",
        "type": "%(levelname)s",
        "service": service_name,
    }

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
