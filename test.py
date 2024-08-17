from typing import List, Union, overload

@overload
def rot13(inp: str) -> str: ...

@overload
def rot13(inp: bytes) -> bytes: ...

def rot13(inp: Union[str, bytes]) -> Union[str, bytes]:
    if isinstance(inp, bytes):
        result: List[int] = []
        for byte in inp:
            if 65 <= byte <= 90:
                result.append((byte - 65 + 13) % 26 + 65)
            elif 97 <= byte <= 122:
                result.append((byte - 97 + 13) % 26 + 97)
            else:
                result.append(byte)
        return bytes(result)
    else:
        return rot13(inp.encode("ascii")).decode("ascii")

print(rot13("Hello, world!"))
