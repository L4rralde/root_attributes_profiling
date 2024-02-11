from component_a import componentA
from component_b import componentB
from component_c import componentC
from component_d import componentD


class Checker:
    def __init__(self) -> None:
        self.current_timestamp: int = None

        self.component_a = componentA(self)
        self.component_b = componentB(self)
        self.component_c = componentC(self)
        self.component_d = componentD(self)

    def quack(self, input):
        input = self.component_a.quack(input)
        input = self.component_b.quack(input)
        input = self.component_c.quack(input)
        input = self.component_c.quack(input)

        return input

    def spin(self):
        self.current_timestamp = 0
        for iteration in range(1, 10000):
            self.quack(None)
            self.current_timestamp += 1000
