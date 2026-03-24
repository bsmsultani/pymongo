from typing import Optional, Any, List, Dict
import struct


class Parser:
    def __init__(self):

        self.buffer : bytearray = bytearray()



    def parse_one(self):
        pass


    def feed(self, chunk : bytearray):

        pass


    


class Serializer:
    def __init__(self):
        pass


    def encode(doc: Dict[str, Any]) -> bytes:
        elements = b''
        for key, val in doc:
            if isinstance(val, str):
                pass

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