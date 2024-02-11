from component import Component

class componentB(Component):
    def __init__(self, root) -> None:
        super().__init__(root)

    def quack(self, input):
        print(f"¨{__name__}: {self.current_timestamp}")
        return input
