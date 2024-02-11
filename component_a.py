class componentA:
    def __init__(self) -> None:
        self.current_timestamp = None

    def quack(self, input):
        for _ in range(100):
            print(f"¨{__name__}: {self.current_timestamp}")
        return input
