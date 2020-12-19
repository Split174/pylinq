from typing import Callable


class Linq:
    def __init__(self, data):
        self.data = data

    def select(self, condition: Callable):
        return Linq(list(filter(condition, self.data)))

    def __len__(self):
        return len(self.data)