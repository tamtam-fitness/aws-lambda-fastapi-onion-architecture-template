class Singleton:
    _unique_instance = None

    @classmethod
    def instance(cls) -> object:
        if cls._unique_instance is None:
            cls._unique_instance = cls()
        return cls._unique_instance

    def __init__(self) -> None:
        if self._unique_instance is not None:
            raise SystemError("Cannot Generate Instance By Constructor")
