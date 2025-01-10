# rate_limiter.py
from limits import RateLimitItemPerMinute
from limits.strategies import FixedWindowRateLimiter
from limits.storage import MemoryStorage
from app.config import Config


class RateLimiter:
    def __init__(self, max_requests, period_seconds):
        # Initialize the rate limiter
        self.rate_limit = RateLimitItemPerMinute(max_requests)
        self.limiter = FixedWindowRateLimiter(MemoryStorage())
        self.period_seconds = period_seconds

    def check_rate_limit(self, key):
        """
        Check if the rate limit has been exceeded for a given key.
        """
        return self.limiter.hit(self.rate_limit, key)

max_requests = 2 if Config.MODE == 'development' else 30
rate_limiter = RateLimiter(max_requests=5, period_seconds=60)
