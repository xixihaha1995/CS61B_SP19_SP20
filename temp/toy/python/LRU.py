import collections

class LRUCache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None
        return value

    def set(self, key, value):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cahce) == self.capacity:
                self.cache.popitem( last == False )
                self.cache[key] = value
            else:
                self.cache[key] = value
