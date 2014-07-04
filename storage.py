import time

class Storage:
    def __init__(self, size):
        self.store = dict()
        self.size = size
    def put(self, key, value):
        if key not in self.store and len(self.store.keys()) == self.size:
            now = time.time()
            oldest = None, now
            for k, v in self.store.items():
                if v[1] < oldest[1]:
                    oldest = k, v[1]
            print "Oldest: ", oldest
            del self.store[oldest[0]]
        self.store[key] = value, time.time()

    def get(self, key):
        self.store[key] = self.store[key][0], time.time()
        return self.store[key][0]
