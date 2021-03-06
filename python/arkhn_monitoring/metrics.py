from functools import wraps

from prometheus_client import Counter as PromCounter, Histogram


class Timer:
    """
    Class to be used as a decorator to time functions and store observation in
    a Prometheus histogram.
    """

    def __init__(self, *args, **kwargs):
        """ Takes the same arguments as prometheus_client.Histogram """
        self.histogram = Histogram(*args, **kwargs)
        self.labelnames = kwargs.get("labelnames", None)

    def __call__(self, func, *args, **kwargs):
        """ The kwargs whose name are in self.labelnames are used to set the metric labels. """

        @wraps(func)
        def timed(*args, **kwargs):
            if self.labelnames is not None:
                # Add the labels
                labels = {k: kwargs[k] for k in self.labelnames}
                hist = self.histogram.labels(**labels)
            else:
                hist = self.histogram

            with hist.time():
                return func(*args, **kwargs)

        return timed


class Counter:
    """
    Class to be used as a decorator to count how many time a function has been called and
    store this value in a Prometheus Counter.
    """

    def __init__(self, *args, **kwargs):
        """ Takes the same arguments as prometheus_client.Counter """
        self.prom_counter = PromCounter(*args, **kwargs)
        self.labelnames = kwargs.get("labelnames", None)

    def __call__(self, func, *args, **kwargs):
        """ The kwargs whose name are in self.labelnames are used to set the metric labels. """

        @wraps(func)
        def counted(*args, **kwargs):
            if self.labelnames is not None:
                # Add the labels
                labels = {k: kwargs[k] for k in self.labelnames}
                self.prom_counter.labels(**labels).inc()
            else:
                self.prom_counter.inc()

            return func(*args, **kwargs)

        return counted


FAST_FN_BUCKETS = (0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5)
