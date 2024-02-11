class Component:
    def __init__(self, root) -> None:
        self._root = root

    @property
    def current_timestamp(self):
        return self._root.current_timestamp
