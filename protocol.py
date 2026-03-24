from multiprocessing import Value
from typing import Optional, Any, List, Dict
import struct


class Parser:
    def __init__(self):

        self._buffer : bytearray = bytearray()
        self._pos : int = 0


    def read_byte(self) -> int:
        if self._pos >= len(self._buffer):
            return

        byte = self._buffer[self._pos]
        self._pos += 1
        return byte
    


class Serializer:
    def __init__(self):
        pass



    @staticmethod
    def _encode_string(value: str) -> bytes:
        """
        Args:
            value : a simple string such as "apple"
        
        Returns:
            [4 byte length][data] data is encoded with utf-8
        """
        return struct.pack("<i", len(value) + 4) + value.encode("utf-8")

    @staticmethod
    def _encode_int(value : int) -> bytes:
        """
        Args:
            value: an integer such as 42
        Returns:
            []
        """
        value = str(value)
        return struct.pack("<i", len(value) + 4) + value.encode("utf-8")


    def encode(doc: Dict[str, Any]) -> bytes:
        elements = b''
        for key, val in doc.items():
            if isinstance(val, str):
                elements += Serializer._encode_string(val)
            elif isinstance(val, int):
                elements += Serializer._encode_int(val)

            elif isinstance(val, bool):
                pass

            elif isinstance(val, dict):
                pass

            elif isinstance(val, list):
                pass

            else:
                raise TypeError(f"Unsupported type: {type(val)} for key {key}")


        total = elements + b"\x00"
        return struct.pack("<i", len(total) + 4) + total  # include 4 bytes of l



if __name__ == "__main__":
    result = Serializer.encode({'name' : 'bismillah', 'age': 21})
    print(result)