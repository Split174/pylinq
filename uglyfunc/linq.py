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

    def distinct(self):
        return Linq(set(self.data))

    def reverse(self):
        return Linq(self.data[::-1])

    def all(self, condition: Callable = lambda x: x) -> bool:
        current_len = len(self)
        number_condition = len(list(filter(condition, self.data)))
        return current_len == number_condition

    def any(self, condition: Callable = lambda x: x) -> bool:
        return False if self.where(condition).to_list() == [] else True

    def __len__(self):
        return len(self.data)

    def to_list(self):
        return self.data



