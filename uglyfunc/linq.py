from typing import Callable
from collections.abc import Iterable


class Linq:
    def __init__(self, data: Iterable):
        self.data = [d for d in data]

    def select(self, condition: Callable = lambda x: x):
        return Linq([condition(item) for item in self.data])

    def where(self, condition: Callable = lambda x: x):
        return Linq(filter(condition, self.data))

    def order_by(self, condition: Callable = lambda x: x):
        return Linq(sorted(self.data, key=condition))

    def order_by_descending(self, condition: Callable = lambda x: x):
        return Linq(sorted(self.data, key=condition, reverse=True))

    def distinct(self):
        return Linq(set(self.data))

    def reverse(self):
        return Linq(self.data[::-1])

    def all(self, condition: Callable = lambda x: x) -> bool:
        current_len = len(self)
        number_condition = len(self.where(condition))
        return current_len == number_condition

    def any(self, condition: Callable = lambda x: x) -> bool:
        return any(condition(d) for d in self.data)

    def count(self, condition: Callable = lambda x: x) -> int:
        return len(self.where(condition))

    def __len__(self):
        return len(self.data)

    def to_list(self):
        return self.data



