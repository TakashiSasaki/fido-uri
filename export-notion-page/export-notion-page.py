"""
このスクリプトは、Github Actionsでシークレットや変数が正しく取得できているかを確認し、
Notion APIを使用してページの内容を取得し、Markdown形式で保存します。

環境変数:
    - NOTION_API_KEY: Notion APIの認証キー
    - PAGE_ID: NotionのページID
    - FILE_NAME: 保存先のファイル名

作成者:
    Takashi SASAKI
    ホームページ: https://x.com/TakashiSasaki
"""

import os
import requests
import tempfile
import json
from dotenv import load_dotenv, find_dotenv

# .envファイルが存在する場合のみ読み込む
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)

def get_env_variable(var_name):
    """
    環境変数を取得する。存在しない場合は例外を投げる。

    Args:
        var_name (str): 環境変数名

    Returns:
        str: 環境変数の値
    """
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"Environment variable {var_name} not found.")
    return value

# 環境変数の取得
try:
    NOTION_API_KEY = get_env_variable('NOTION_API_KEY')
    NOTION_PAGE_ID = get_env_variable('NOTION_PAGE_ID')
    NOTION_MD_FILE_NAME = get_env_variable('NOTION_MD_FILE_NAME')
except EnvironmentError as e:
    print(e)
    exit(1)

# デバッグ出力
print(f"NOTION_API_KEY: {NOTION_API_KEY}")
print(f"NOTION_PAGE_ID: {NOTION_PAGE_ID}")
print(f"NOTION_MD_FILE_NAME: {NOTION_MD_FILE_NAME}")

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_page_content(page_id):
    """
    指定されたページIDからNotionのページ内容を取得する。

    Args:
        page_id (str): NotionのページID

    Returns:
        dict: ページの内容を含むJSONレスポンス
        None: エラー発生時
    """
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content}")
    return response.json()

def notion_to_markdown(content):
    """
    Notionのページ内容をMarkdown形式に変換する。

    Args:
        content (dict): Notionのページ内容

    Returns:
        str: Markdown形式のテキスト
    """
    if not content:
        return ""

    markdown = ""
    for block in content["results"]:
        block_type = block["type"]
        text = block.get(block_type, {}).get("rich_text", [])

        if block_type == "paragraph":
            markdown += "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "heading_1":
            markdown += "# " + "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "heading_2":
            markdown += "## " + "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "heading_3":
            markdown += "### " + "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "bulleted_list_item":
            markdown += "- " + "".join([t["plain_text"] for t in text]) + "\n"

        elif block_type == "numbered_list_item":
            markdown += "1. " + "".join([t["plain_text"] for t in text]) + "\n"

        elif block_type == "quote":
            markdown += "> " + "".join([t["plain_text"] for t in text]) + "\n\n"

        elif block_type == "code":
            language = block["code"].get("language", "")
            markdown += f"```{language}\n" + "".join([t["plain_text"] for t in text]) + "\n```\n\n"

        elif block_type == "image":
            image_url = block["image"]["file"]["url"]
            markdown += f"![image]({image_url})\n\n"

        elif block_type == "bookmark":
            bookmark_url = block["bookmark"]["url"]
            markdown += f"[Bookmark]({bookmark_url})\n\n"

        elif block_type == "table_of_contents":
            markdown += "[Table of Contents]\n\n"

        elif block_type == "link_preview":
            link_url = block["link_preview"]["url"]
            markdown += f"[Link Preview]({link_url})\n\n"

        # Add more block types as needed

    return markdown

# Notionページ内容の取得
content = get_page_content(NOTION_PAGE_ID)
if content:
    # 一時ファイルにJSONデータを保存
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix='.json') as temp_file:
        json.dump(content, temp_file, ensure_ascii=False, indent=4)
        temp_file_path = temp_file.name
        print(f"JSON content saved to temporary file: {temp_file_path}")

    markdown_content = notion_to_markdown(content)

    # 保存先のファイル名を取得し、Markdown内容を保存
    try:
        with open(NOTION_MD_FILE_NAME, "w", encoding="utf-8") as file:
            file.write(markdown_content)
        print("Markdown export complete.")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")
else:
    print("Failed to retrieve content from Notion.")
