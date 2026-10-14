"""Practice an LRU cache using OrderedDict."""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self.capacity = capacity
        self.items: OrderedDict[object, object] = OrderedDict()

    def get(self, key: object) -> object | None:
        if key not in self.items:
            return None
        self.items.move_to_end(key)
        return self.items[key]

    def put(self, key: object, value: object) -> None:
        self.items[key] = value
        self.items.move_to_end(key)
        if len(self.items) > self.capacity:
            self.items.popitem(last=False)


def main() -> None:
    cache = LRUCache(2)
    cache.put("a", 10)
    cache.put("b", 20)
    cache.get("a")
    cache.put("c", 30)
    print("a:", cache.get("a"))
    print("b:", cache.get("b"))
    print("c:", cache.get("c"))


if __name__ == "__main__":
    main()