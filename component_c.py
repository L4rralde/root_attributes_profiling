from component import Component


class componentC(Component):
    def __init__(self, root) -> None:
        super().__init__(root)

    def quack(self, input):
        for _ in range(1000):
            print(f"¨{__name__}: {self.current_timestamp}")
        return input
