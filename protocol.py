from multiprocessing import Value
from typing import Optional, Any, List, Dict
import struct


class Incomplete(Exception):
    pass


class Parser:
    def __init__(self):

        self._buffer : bytearray = bytearray()
        self._pos : int = 0


    def feed(self, byte_info : bytes) -> int:
        self._buffer.extend(byte_info)



    def read_byte(self) -> int:
        if self._pos >= len(self._buffer):
            return

        byte = self._buffer[self._pos]
        self._pos += 1
        return byte

    def _parse_one(self) -> bytes:
        """
        Try to parse one complete BSON message from the buffer.
        """
        if self._pos >= len(self._buffer):
            return None
        
        saved_pos = self._pos
        try:
            result = self._parse_next()
            self._pos = 0
            self._buffer = self._buffer[self._pos:]
            return result

        except Incomplete:
            self._pos = saved_pos
            return None
        

    def _parse_next(self):

        type_byte = self.read_byte()

        if type_byte == 1:
            print("this is a string type")
    


class Serializer:
    def __init__(self):
        pass



    @staticmethod
    def _encode_string(key : str, value: str) -> bytes:
        """
        Args:
            key : the key
            value : a simple string such as "apple"
        
        Returns:
            [4 byte length][data] data is encoded with utf-8
        """
        key_bytes = key.encode('utf-8') + b"\x00"
        value_bytes = value.encode('utf-8')
        return bytes([1]) + key_bytes + struct.pack("<i", len(value_bytes) + 4) + value_bytes


    def encode(doc: Dict[str, Any]) -> bytes:
        elements = b''
        for key, val in doc.items():
            if isinstance(val, str):
                elements += Serializer._encode_string(key, val)
            elif isinstance(val, int):
                pass

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
    result = Serializer.encode({'name' : 'john', 'age': 21})
    parser = Parser()
    parser.feed(result)
    parser._parse_one()