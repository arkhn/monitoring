# Python package

You can install this package with `pip install arkhn-monitoring`.

## Usage

```
from arkhn_monitoring import Counter, Timer

@Timer(<args and kwargs for prometheus client Histogram>)
def func_to_time():
    ...

@Counter(<args and kwargs for prometheus client Counter>)
def func_to_count():
    ...
```