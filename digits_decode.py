def digits_decode(encoded: str) -> bytes:
    """
    Decode a string of digits into a byte sequence.

    This function decodes the digit sequence from a FIDO URI back into a CBOR byte sequence. 
    It processes the encoded string in chunks, converting each chunk to an integer, then 
    to bytes, and finally extracts the relevant bytes to form the original byte sequence.

    Args:
        encoded (str): The string of digits to decode.

    Returns:
        bytes: The decoded byte sequence.
    """
    chunk_digits = 17
    decoded = b""
    while len(encoded) >= chunk_digits:
        chunk_str = encoded[:chunk_digits]
        value = int(chunk_str)
        chunk = value.to_bytes(8, 'little')[:7]  # Take only the first 7 bytes
        decoded += chunk
        encoded = encoded[chunk_digits:]

    if len(encoded) != 0:
        partial_chunk_digits = 0x0fda8530
        for i in range(1, 7):
            if len(encoded) == ((partial_chunk_digits >> (4 * i)) & 0xF):
                value = int(encoded)
                chunk = value.to_bytes(8, 'little')[:i]
                decoded += chunk
                break

    return decoded

if __name__ == "__main__":
    from digits_encode import digits_encode
    data = b'1234567abcdef'
    encoded = digits_encode(data)
    print(f"Encoded: {encoded}")

    decoded = digits_decode(encoded)
    print(f"Decoded: {decoded}")
    print(f"Original and decoded are the same: {data == decoded}")
