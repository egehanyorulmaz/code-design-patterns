class Cache:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # inheriting from the built-in object class in Python
            # ensure that only one instance of a class exists
            # and provides a global point of access to that instance.
            cls._instance = super(Cache, cls).__new__(cls)
            cls._instance._cache = {}
        return cls._instance

    def set(self, key, value):
        self._cache[key] = value

    def get(self, key):
        return self._cache.get(key)

    def contains(self, key):
        return key in self._cache


# Usage Example
cache = Cache()
cache.set("result_42", 123456)

# Retrieve the value from another part of the code
cache2 = Cache()
print(cache2.get("result_42"))  # Output: 123456

# Since it's a Singleton, both instances are actually the same object
assert cache is cache2
