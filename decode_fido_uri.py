from digits_decode import digits_decode
import cbor2
import json

def decode_fido_uri(uri: str) -> dict:
    """
    指定されたFIDO URIをデコードし、CBORバイト列をデコードして辞書形式のデータを取得する。

    Args:
        uri (str): FIDO URI文字列。

    Returns:
        dict: デコードされたCBORデータ。
    """
    # FIDO URIをデコードしてCBORバイト列を取得
    decoded: bytes = digits_decode(uri)

    # CBORバイト列をデコードして辞書形式のデータを取得
    decoded_data: dict = cbor2.loads(decoded)
    
    return decoded_data

def main():
    """
    メイン関数。指定されたFIDO URIをデコードし、デコードされたデータを表示する。
    """
    # デコードするFIDO URI
    fido_uri = "144519942798050940878582488612106138031714230513094139379299368895081878828178926639100664952474023496122943190653681470073382838502067711648524250383106107096654083332"

    # FIDO URIをデコードしてデコードされたデータを取得
    decoded_data = decode_fido_uri(fido_uri)

    # デコードされたデータを表示
    print(decoded_data)

if __name__ == "__main__":
    main()
