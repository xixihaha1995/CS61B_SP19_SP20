import collections

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None
        return value

    def set(self, key, value):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last = False )
                self.cache[key] = value
            else:
                self.cache[key] = value


c = LRUCache(5)

for i in range(5, 10):
    c.set(i, 10 * i)

print(c.cache)