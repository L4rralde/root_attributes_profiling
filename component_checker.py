from component_a import componentA
from component_b import componentB
from component_c import componentC
from component_d import componentD


class Checker:
    def __init__(self) -> None:
        self._current_timestamp: int = None

        self.component_a = componentA()
        self.component_b = componentB()
        self.component_c = componentC()
        self.component_d = componentD()

    @property
    def current_timestamp(self):
        return self._current_timestamp

    @current_timestamp.setter
    def current_timestamp(self, time):
        self._current_timestamp = time
        self.component_a.current_timestamp = time
        self.component_b.current_timestamp = time
        self.component_c.current_timestamp = time
        self.component_d.current_timestamp = time

    def quack(self, input):
        input = self.component_a.quack(input)
        input = self.component_b.quack(input)
        input = self.component_c.quack(input)
        input = self.component_d.quack(input)

        return input

    def spin(self):
        self.current_timestamp = 0
        for iteration in range(1, 500):
            for _ in range(10):
                self.quack(None)
            self.current_timestamp += 1000
