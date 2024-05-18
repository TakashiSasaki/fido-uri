import struct

def digits_encode(data: bytes) -> str:
    """
    Encode a byte sequence into a string of digits.

    This function encodes CBOR byte sequences when generating FIDO URIs. It converts
    the given byte sequence into a sequence of digits by processing the data in chunks,
    extending each chunk to 8 bytes, converting it to an integer, and then formatting it
    as a zero-padded string.

    Args:
        data (bytes): The byte sequence to encode.

    Returns:
        str: The encoded string of digits.
    """
    chunk_size = 7
    chunk_digits = 17
    zeros = "00000000000000000"

    ret = ""
    while len(data) >= chunk_size:
        chunk = data[:chunk_size] + b'\x00'  # Extend to 8 bytes
        value = int.from_bytes(chunk, 'little')
        v = str(value)
        ret += zeros[:chunk_digits - len(v)]
        ret += v
        data = data[chunk_size:]

    if len(data) != 0:
        partial_chunk_digits = 0x0fda8530
        digits = (partial_chunk_digits >> (4 * len(data))) & 0xF
        chunk = data + b'\x00' * (8 - len(data))
        value = int.from_bytes(chunk, 'little')
        v = str(value)
        ret += zeros[:digits - len(v)]
        ret += v

    return ret

if __name__ == "__main__":
    from digits_decode import digits_decode
    data = b'1234567abcdef'
    encoded = digits_encode(data)
    print(f"Encoded: {encoded}")

    decoded = digits_decode(encoded)
    print(f"Decoded: {decoded}")
    print(f"Original and decoded are the same: {data == decoded}")
