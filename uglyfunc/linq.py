from typing import Callable
from collections.abc import Iterable


class Linq:
    def __init__(self, data: Iterable):
        self.data = [d for d in data]

    def select(self, condition: Callable = lambda x: x):
        return Linq(Linq._select(self.data, condition))

    def where(self, condition: Callable = lambda x: x):
        return Linq(filter(condition, self.data))

    def order_by(self, condition: Callable = lambda x: x):
        return Linq(sorted(self.data, key=condition))

    def order_by_descending(self, condition: Callable = lambda x: x):
        return Linq(sorted(self.data, key=condition, reverse=True))

    def distinct(self):
        return Linq(set(self.data))

    def distinct_by(self, condition: Callable = lambda x: x):
        new_data = []
        for d in self.data:
            if condition(d) not in Linq._select(new_data, condition):
                new_data.append(d)
        return Linq(new_data)

    def reverse(self):
        return Linq(self.data[::-1])

    def contains(self, item) -> bool:
        return item in self

    def all(self, condition: Callable = lambda x: x) -> bool:
        current_len = len(self)
        number_condition = len(self.where(condition))
        return current_len == number_condition

    def any(self, condition: Callable = lambda x: x) -> bool:
        return any(condition(d) for d in self.data)

    def count(self, condition: Callable = lambda x: x) -> int:
        return len(self.where(condition))

    def first(self, condition: Callable = lambda x: x, default=None):
        if len(self) >= 1:
            for d in self.data:
                if condition(d):
                    return Linq([d])
        return default

    def last(self, condition: Callable = lambda x: x, default=None):
        return self.reverse().first(condition, default)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    @staticmethod
    def _select(data, condition: Callable = lambda x: x):
        return [condition(item) for item in data]

    def to_list(self):
        return self.data



