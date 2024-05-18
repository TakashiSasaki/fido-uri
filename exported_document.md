[Table of Contents]

# GithubへのPasskeyによるログインの開始



Sign in with a passkeyを選択するとパスキーでの認証が始まる。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/105fd01d-db5b-4c90-8c22-09bb5d59779d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240518T093546Z&X-Amz-Expires=3600&X-Amz-Signature=a74b4f74123490b11a8a1b0504fc4d257dfa5c79a71e6ebbda27972f846f2b4a&X-Amz-SignedHeaders=host&x-id=GetObject)

新しい認証器を登録するには「iPhone、iPad、またはAndroidデバイス」を選択する。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/45b1958d-789f-495b-81e7-4544b31dcfa4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240518T093546Z&X-Amz-Expires=3600&X-Amz-Signature=113827c2aa9ecd59721fc33bcfeb064da5d05b60331f432eb058e301f12d61a1&X-Amz-SignedHeaders=host&x-id=GetObject)

QRコードが表示される。これがハイブリッドトランスポートである。

つまりFIDO2で使われるCTAPの基本的なトランスポートは近接性を確認できるWi-Fi、USB、Bluetooth LEであるが、それと併用できる別のトランスポートも使用するのがハイブリッドトランスポートであり、その手段の一つとしてQRコードがある、ということである。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/c6b1537b-a6ab-44d2-80c0-a42758166c29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240518T093546Z&X-Amz-Expires=3600&X-Amz-Signature=96d625da41f6da99300f15c0addc4de23ee67d8bd91fae34edf99be9c8a3df4c&X-Amz-SignedHeaders=host&x-id=GetObject)

# FIDOスキームのURI

QRコードをデコードすると以下のようなFIDOスキームのURIになる。

```javascript
FIDO:/144519942798050940878582488612106138031714230513094139379299368895081878828178926639100664952474023496122943190653681470073382838502067711648524250383106107096654083332
```

FIDO:/ の部分が英数字モードでエンコードされ、その後数字モードでエンコードされることを想定している。これによりQRコードのサイズを小さくすることができる。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/67a54c04-6d13-4849-8ba8-37d1d2938e99/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240518T093546Z&X-Amz-Expires=3600&X-Amz-Signature=22669eb3fc7baa210d129f9b2146c5e4904ba0f4f47715653f6af90f81e18b79&X-Amz-SignedHeaders=host&x-id=GetObject)

# Bluetoothの必要性

PCでGithubを開いてスマートフォンなどローミング認証機によりPasskey認証を行おうと思うとBluetooth接続を一時的に有効にするよう求められる。

このことからBluetoothによる近接性の確認が行われていることが確認できる。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/c516ef43-599e-4129-af2e-4e1d4ed8f613/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240518T093546Z&X-Amz-Expires=3600&X-Amz-Signature=f0bfea80bed720050853d2d4b78f4e11a976a3b6dd5afe79b0c9bd15fd3df378&X-Amz-SignedHeaders=host&x-id=GetObject)

# FIDOスキームURIのデコード

ハイブリッドトランスポートで使われるFIDO URIの数字部分は、CBORによりシリアライズされたデータをエンコードしたものである。

エンコードは7バイトを17桁の数字にエンコードしている。

> エンコーディングはQRコード内で効率的に表現されるように設計されています。7バイトの塊はリトルエンディアンの値として解釈され、17桁の10進数としてエンコードされます。残りのバイトは、同様にそのバイト数の値が必要とする最小限の桁数を使用してエンコードされます。具体的には、残りのバイト数が1, 2, 3, 4, 5, または 6バイトであることがわかっているため、そのエンコード形式はそれぞれ3桁、5桁、8桁、10桁、13桁、または15桁になります。

[Link Preview](https://github.com/TakashiSasaki/fido-uri)

# 規格文書

[Bookmark](https://fidoalliance.org/specs/fido-v2.2-rd-20230321/fido-client-to-authenticator-protocol-v2.2-rd-20230321.html)



