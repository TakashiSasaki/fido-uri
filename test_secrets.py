"""
このスクリプトはGithub Actionsでシークレットや変数が本当に取得できているか確認するためのものです。
Pythonスクリプト側ではあくまでも環境変数としてみているだけであって、
シークレットや変数を環境変数にマップするのはGithub ActionsのYAMLファイルの側での責任。

環境変数から以下のシークレットを取得し、デバッグ出力を行います:
    - NOTION_API_KEY
    - PAGE_ID
    - FILE_NAME

使用方法:
    Github Actionsのワークフロー内でこのスクリプトを実行し、シークレットや変数が正しく取得されているかを確認します。

出力:
    環境変数 `NOTION_API_KEY`、`PAGE_ID` および `FILE_NAME` の値を出力します。

依存関係:
    - os モジュール

作成者:
    Takashi SASAKI
    ホームページ: https://x.com/TakashiSasaki
"""

import os

# 環境変数の取得
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
PAGE_ID = os.getenv('PAGE_ID')
FILE_NAME = os.getenv('FILE_NAME')

# デバッグ出力
print(f"NOTION_API_KEY: {NOTION_API_KEY}")
print(f"PAGE_ID: {PAGE_ID}")
print(f"FILE_NAME: {FILE_NAME}")
