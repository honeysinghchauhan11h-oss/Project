class HashMap:
    """
    Course-aligned Hash Map using separate chaining.
    Average-case search/insert/delete is O(1).
    Worst case is O(n) if many keys collide into one bucket.
    """

    def __init__(self, capacity=101):
        self.capacity = max(11, capacity)
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

    def _hash(self, key):
        """
        Basic deterministic string-friendly hash function.
        Avoids relying on Python dict for core storage.
        """
        text = str(key)
        value = 0
        for ch in text:
            value = (value * 31 + ord(ch)) % self.capacity
        return value

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def get(self, key, default=None):
        index = self._hash(key)
        for existing_key, value in self.table[index]:
            if existing_key == key:
                return value
        return default

    def contains(self, key):
        return self.get(key, None) is not None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def keys(self):
        result = []
        for bucket in self.table:
            for key, _ in bucket:
                result.append(key)
        return result

    def __len__(self):
        return self.size
