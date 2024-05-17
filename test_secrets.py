import os

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
PAGE_ID = os.getenv('PAGE_ID')

# デバッグ出力
print(f"NOTION_API_KEY: {NOTION_API_KEY}")
print(f"PAGE_ID: {PAGE_ID}")
