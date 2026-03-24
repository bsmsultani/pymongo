from typing import Optional, Any, List


class Serializer:
    def __init__(self):
        pass


    def encode(value : str) -> bytes:
        return f"+{value}\r\n".encode("utf-8")

    