import time

class Cache:
    def __init__(self, ttl=300): #5 minutes
        self.ttl = ttl
        self.store = {}

    def get(self, key):
        if key in self.store:
            timestamp, value = self.store[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.store[key]
        return None

    def set(self, key, value):
        self.store[key] = (time.time(), value)
