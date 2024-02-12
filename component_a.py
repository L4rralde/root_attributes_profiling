from component import Component

class componentA(Component):
    def __init__(self, root) -> None:
        super().__init__(root)

    def quack(self, input):
        for _ in range(100):
            print(f"¨{__name__}: {self.current_timestamp}")
        return input
