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
import sys

# 環境変数の取得
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_PAGE_ID = os.getenv('NOTION_PAGE_ID')
NOTION_MD_FILE_NAME = os.getenv('NOTION_MD_FILE_NAME')

# 初期化
exit_code = 0

# エラーハンドリングとデバッグ出力
if NOTION_API_KEY is None:
    print("Error: NOTION_API_KEY is not set.")
    exit_code = 1
else:
    print(f"NOTION_API_KEY: {NOTION_API_KEY[:4]}...")  # シークレット情報の一部のみを表示

if NOTION_PAGE_ID is None:
    print("Error: NOTION_PAGE_ID is not set.")
    exit_code = 1
else:
    print(f"NOTION_PAGE_ID: {NOTION_PAGE_ID}")

if NOTION_MD_FILE_NAME is None:
    print("Error: NOTION_MD_FILE_NAME is not set.")
    exit_code = 1
else:
    print(f"NOTION_MD_FILE_NAME: {NOTION_MD_FILE_NAME}")

# スクリプトの終了時に適切なエラーコードを返す
sys.exit(exit_code)
