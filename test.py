from typing import List

def rot13(b: bytes) -> bytes:
    result: List[int] = []
    for byte in b:
        if 65 <= byte <= 90:
            result.append((byte - 65 + 13) % 26 + 65)
        elif 97 <= byte <= 122:
            result.append((byte - 97 + 13) % 26 + 97)
        else:
            result.append(byte)
    return bytes(result)

def crypt(s: str) -> str:
    b: bytes = s.encode('ascii')
    roted: bytes = rot13(b)
    return roted.decode('ascii')

print(crypt("Hello, world!"))