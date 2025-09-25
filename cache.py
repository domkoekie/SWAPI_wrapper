import time

#ttl = time-to-live
class Cache:
    def __init__(self, ttl=300): #stay in cache for 5 minutes
        self.ttl = ttl
        self.store = {}

    def get(self, key):
        if key in self.store:
            timestamp, value = self.store[key]
            if time.time() - timestamp < self.ttl:
                return value #returns value if not expired
            else:
                del self.store[key] #deletes expired item
        return None

    def set(self, key, value):
        self.store[key] = (time.time(), value) #saves value with timestamp in cache
