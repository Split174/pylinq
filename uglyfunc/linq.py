from typing import Callable


class Linq:
    def __init__(self, data):
        self.data = data

    def select(self, condition: Callable):
        pass

    def __len__(self):
        return len(self.data)