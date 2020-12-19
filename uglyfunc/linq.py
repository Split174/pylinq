from typing import Callable


class Linq:
    def __init__(self, data):
        self.data = [d for d in data]

    def select(self, condition: Callable):
        return Linq([condition(item) for item in self.data])

    def where(self, condition: Callable):
        return Linq(list(filter(condition, self.data)))

    def order_by(self, condition: Callable):
        return Linq(list(sorted(self.data, key=condition)))

    def __len__(self):
        return len(self.data)

    def to_list(self):
        return self.data

