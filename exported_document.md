# GithubへのPasskeyによるログインの開始



Sign in with a passkeyを選択するとパスキーでの認証が始まる。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/105fd01d-db5b-4c90-8c22-09bb5d59779d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240517T032047Z&X-Amz-Expires=3600&X-Amz-Signature=ec1a26f9e971a7b9bb4f37a1d876f0b20e90330035efb6a19186b78e48dc3504&X-Amz-SignedHeaders=host&x-id=GetObject)

新しい認証器を登録するには「iPhone、iPad、またはAndroidデバイス」を選択する。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/45b1958d-789f-495b-81e7-4544b31dcfa4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240517T032047Z&X-Amz-Expires=3600&X-Amz-Signature=b0c1d638dd4a083251ea85b7a63f7bb74b3c1fc9f23dd1f6a3cbbcbc8c8dfe94&X-Amz-SignedHeaders=host&x-id=GetObject)

QRコードが表示される。これがハイブリッドトランスポートである。

つまりFIDO2で使われるCTAPの基本的なトランスポートは近接性を確認できるWi-Fi、USB、Bluetooth LEであるが、それと併用できる別のトランスポートも使用するのがハイブリッドトランスポートであり、その手段の一つとしてQRコードがある、ということである。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/c6b1537b-a6ab-44d2-80c0-a42758166c29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240517T032047Z&X-Amz-Expires=3600&X-Amz-Signature=cd0954753ad76faac43b0340f10c2bb96ff202811975d9671d83629d1a349cd8&X-Amz-SignedHeaders=host&x-id=GetObject)

# FIDOスキームのURI

QRコードをデコードすると以下のようなFIDOスキームのURIになる。

```javascript
FIDO:/144519942798050940878582488612106138031714230513094139379299368895081878828178926639100664952474023496122943190653681470073382838502067711648524250383106107096654083332
```

FIDO:/ の部分が英数字モードでエンコードされ、その後数字モードでエンコードされることを想定している。これによりQRコードのサイズを小さくすることができる。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/67a54c04-6d13-4849-8ba8-37d1d2938e99/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240517T032047Z&X-Amz-Expires=3600&X-Amz-Signature=5ed5ee7be66352b1c7305bb3a5f56305d5d0892176805d0341df742954017948&X-Amz-SignedHeaders=host&x-id=GetObject)

# Bluetoothの必要性

PCでGithubを開いてスマートフォンなどローミング認証機によりPasskey認証を行おうと思うとBluetooth接続を一時的に有効にするよう求められる。

このことからBluetoothによる近接性の確認が行われていることが確認できる。

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/f74817d1-981d-4a9d-bf70-0ecc1d271f27/c516ef43-599e-4129-af2e-4e1d4ed8f613/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240517T032047Z&X-Amz-Expires=3600&X-Amz-Signature=fb115d9a9e5d7fe5d6c5dfe481a9d1027f4ac044cce062ef0b09031e6c0ba341&X-Amz-SignedHeaders=host&x-id=GetObject)

# FIDOスキームURIのデコード

ハイブリッドトランスポートで使われるFIDO URIの数字部分は、CBORによりシリアライズされたデータをエンコードしたものである。

エンコードは7バイトを17桁の数字にエンコードしている。

> エンコーディングはQRコード内で効率的に表現されるように設計されています。7バイトの塊はリトルエンディアンの値として解釈され、17桁の10進数としてエンコードされます。残りのバイトは、同様にそのバイト数の値が必要とする最小限の桁数を使用してエンコードされます。具体的には、残りのバイト数が1, 2, 3, 4, 5, または 6バイトであることがわかっているため、そのエンコード形式はそれぞれ3桁、5桁、8桁、10桁、13桁、または15桁になります。

# 規格文書

[Bookmark](https://fidoalliance.org/specs/fido-v2.2-rd-20230321/fido-client-to-authenticator-protocol-v2.2-rd-20230321.html)



