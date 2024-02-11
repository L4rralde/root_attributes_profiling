class Component:
    def __init__(self, root) -> None:
        self._root = root

    def __getattr__(self, attr):
        return getattr(self._root, attr)
