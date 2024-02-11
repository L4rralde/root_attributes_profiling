class componentB:
    def __init__(self, root) -> None:
        self.root = root

    def quack(self, input):
        for _ in range(1000):
            print(f"¨{__name__}: {self.root.current_timestamp}")
        return input
