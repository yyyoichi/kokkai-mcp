


class KokkkaiAPIRequestConfig:
    """
    Configuration class for request settings.
    """
    def __init__(self, usecache: bool = False, interval_milsec: int = 1000):
        self.usecache = usecache
        self.interval_milsec = interval_milsec
