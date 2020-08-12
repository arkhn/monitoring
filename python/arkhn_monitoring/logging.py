from fluent import handler
import logging


class CustomFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, "resource_id"):
            record.resource_id = None
        return True


def create_fluent_logger(service_name, fluentd_host, fluentd_port, level=None):
    custom_format = {
        "where": "%(module)s.%(funcName)s",
        "type": "%(levelname)s",
        "service": service_name,
        "resource_id": "%(resource_id)s",
    }

    logger = logging.getLogger(service_name)
    logger.propagate = False

    h = handler.FluentHandler(service_name, host=fluentd_host, port=fluentd_port)
    formatter = handler.FluentRecordFormatter(custom_format)
    h.setFormatter(formatter)
    logger.addHandler(h)
    logger.addFilter(CustomFilter())
    logger.setLevel(level or getattr(logging, level))

    return logger
