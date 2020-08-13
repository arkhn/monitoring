# Python package

You can install this package with `pip install arkhn-monitoring`.

## Metrics

```
from arkhn_monitoring import Counter, Timer

@Timer(<args and kwargs for prometheus client Histogram>)
def func_to_time():
    ...

@Counter(<args and kwargs for prometheus client Counter>)
def func_to_count():
    ...
```

## Logging

```
from arkhn_monitoring import create_logger

logger = create_logger(
    "service",
    fluentd_host="fluentd",
    fluentd_port=24224,
    level="DEBUG",
    extra_fields=["resource_ids"]
)

logger.debug("log")
```
