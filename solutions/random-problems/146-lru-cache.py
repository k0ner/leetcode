from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._data = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self._data:
            return -1

        self.accessed(key)
        return self._data[key]

    def put(self, key: int, value: int) -> None:
        if not self.capacity and key not in self._data:
            self.evict()

        if key not in self._data:
            self.capacity -= 1

        self._data[key] = value
        self.accessed(key)

    def evict(self):
        self._data.popitem(last=False)
        self.capacity += 1

    def accessed(self, key):
        self._data.move_to_end(key)

    # Your LRUCache object will be instantiated and called as such:


if __name__ == '__main__':
    _data = OrderedDict()

    obj = LRUCache(2)
    obj.put(1, 0)
    obj.put(2, 2)
    obj.get(1)
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    obj.get(3)
    obj.get(4)
