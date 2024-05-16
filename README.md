# README

## 概要

このJupyter Notebookは、CBORデータを特定の形式の数字列に変換する「Digits Encoding」について説明し、その実装と動作確認を行っています。

具体的には、以下の内容を含んでいます：

1. **Digits Encodingの実装**: 
   - バイト列を17桁の数字列にエンコードする関数`digit_encode`。
   - エンコードされた数字列をバイト列にデコードする関数`digit_decode`。

2. **ラウンドトリップ確認**:
   - `digit_encode`と`digit_decode`がバイナリデータに対して正しく動作することを確認。

3. **実際のFIDO URIのデコード**:
   - 生成されたFIDO URIの数字部分をデコードし、その内容を確認。

このNotebookでは、上記の各機能について詳細な実装コードとその動作確認が行われています。
